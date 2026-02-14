require("dotenv").config({ path: ".env.local" });
const path = require("path");
const express = require("express");
const cors = require("cors");
const crypto = require("crypto");
const { createServer } = require("http");
const { Server } = require("socket.io");
const { PREDEFINED_GAMES } = require("./games");
const { APP_CONFIG } = require("./config");
const persist = require("./persistence-bridge");
const pool = require("./db");

const HOST_SECRET = process.env.HOST_PASSWORD || APP_CONFIG.hostPasswordHint || "teachISO!";

const PORT = process.env.PORT || 3000;

const app = express();
app.use(cors());
app.use(express.json());

// Default landing page is English
app.get("/", (req, res) => res.redirect("/index_en.html"));

app.use(express.static(__dirname));

const httpServer = createServer(app);
const io = new Server(httpServer, {
    cors: {
        origin: "*"
    }
});

const sessions = new Map();
const authorizedHosts = new Set();

const leaveRoomIfPossible = (socketId, code) => {
    const client = io.sockets.sockets.get(socketId);
    if (client) {
        client.leave(toRoom(code));
    }
};

const removePlayerFromSessions = (socketId) => {
    sessions.forEach((session) => {
        if (session.players.has(socketId)) {
            session.players.delete(socketId);
            leaveRoomIfPossible(socketId, session.code);
            publishPlayerList(session);
        }
    });
};

const generateSessionCode = () => {
    const alphabet = "ABCDEFGHJKMNPQRSTUVWXYZ23456789";
    let code = "";
    do {
        code = Array.from({ length: 5 }, () => alphabet[Math.floor(Math.random() * alphabet.length)]).join("");
    } while (sessions.has(code));
    return code;
};

const getPredefinedGame = (gameId) => {
    if (gameId) {
        return PREDEFINED_GAMES.find(game => game.game_id === gameId) || null;
    }
    return PREDEFINED_GAMES[0] || null;
};

const toRoom = (code) => code;

const safeString = (value, fallback = "") => {
    if (!value || typeof value !== "string") return fallback;
    return value.trim();
};

const shuffleArray = (arr) => {
    for (let i = arr.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [arr[i], arr[j]] = [arr[j], arr[i]];
    }
    return arr;
};

const getQuestionPayload = (question, language) => {
    const makeVariant = (field) => ({
        es: question[`${field}_es`],
        en: question[`${field}_en`]
    });
    return {
        id: question.id,
        iso_standard: question.iso_standard,
        difficulty: question.difficulty,
        context: makeVariant("context"),
        question: makeVariant("question"),
        options: {
            es: question.options_es,
            en: question.options_en
        },
        explanation: makeVariant("explanation"),
        correct_index: question.correct_index,
        approvedOptions: question.options_es.length
    };
};

const buildRanking = (session) => {
    const ranking = Array.from(session.players.values()).map(player => {
        const avgTime = player.correctTimeEntries > 0
            ? player.totalTime / player.correctTimeEntries
            : null;
        return {
            nickname: player.nickname,
            score: player.score,
            correctCount: player.correctCount,
            avgTime,
            fastestMs: player.fastestMs,
            socketId: player.socketId
        };
    });

    ranking.sort((a, b) => {
        if (b.score !== a.score) return b.score - a.score;
        const aAvg = a.avgTime ?? Number.POSITIVE_INFINITY;
        const bAvg = b.avgTime ?? Number.POSITIVE_INFINITY;
        return aAvg - bAvg;
    });

    return ranking;
};

const publishPlayerList = (session) => {
    const players = Array.from(session.players.values()).map(p => ({
        nickname: p.nickname,
        score: p.score
    }));
    io.to(session.hostSocketId).emit("session:players", { code: session.code, players });
};

const ensureHost = (socket, code) => {
    if (!authorizedHosts.has(socket.id)) return { error: "UNAUTHORIZED" };
    const session = sessions.get(code);
    if (!session) return { error: "SESSION_NOT_FOUND" };
    if (session.hostSocketId !== socket.id) return { error: "NOT_HOST" };
    return { session };
};

const finalizeQuestion = (session) => {
    const question = session.game.questions[session.questionIndex];
    const ranking = buildRanking(session);
    const totalPlayers = session.players.size;
    let answered = 0;
    let correctAnswers = 0;

    session.players.forEach(player => {
        const response = session.responses.get(player.socketId);
        if (response) {
            answered += 1;
            if (response.correct) correctAnswers += 1;
        }
    });

    const stats = {
        totalPlayers,
        answered,
        correct: correctAnswers,
        incorrect: Math.max(answered - correctAnswers, 0)
    };

    io.to(session.hostSocketId).emit("question:results", {
        questionId: question.id,
        correctIndex: question.correct_index,
        explanation: {
            es: question.explanation_es,
            en: question.explanation_en
        },
        stats,
        rankingTop: ranking.slice(0, 5)
    });

    session.players.forEach(player => {
        const response = session.responses.get(player.socketId);
        io.to(player.socketId).emit("question:feedback", {
            questionId: question.id,
            correct: response ? response.correct : false,
            choice: response ? response.choice : null,
            points: response ? response.points : 0,
            timeMs: response ? response.timeMs : null,
            explanation: {
                es: question.explanation_es,
                en: question.explanation_en
            },
            rankingPosition: ranking.findIndex(r => r.socketId === player.socketId) + 1,
            totalPlayers,
            score: player.score
        });
    });

    io.to(toRoom(session.code)).emit("session:ranking", { ranking });
    publishPlayerList(session);
    session.responses.clear();
    session.questionOpen = false;
};

const emitFinalAwards = (session) => {
    const ranking = buildRanking(session);
    const awards = {};
    if (ranking.length > 0) {
        awards.topScorer = ranking[0];
    }
    if (session.game) {
        const minCorrect = Math.ceil(session.game.questions.length * 0.5);
        const fastestCandidates = ranking.filter(r => r.correctCount >= minCorrect && typeof r.fastestMs === "number");
        fastestCandidates.sort((a, b) => a.fastestMs - b.fastestMs);
        if (fastestCandidates.length > 0) {
            awards.fastest = fastestCandidates[0];
        }
    }

    io.to(toRoom(session.code)).emit("session:final", { ranking, awards });
};

const removeSession = (code) => {
    const session = sessions.get(code);
    if (session) {
        io.to(toRoom(code)).emit("session:ended", { code });
        io.socketsLeave(toRoom(code));
        sessions.delete(code);
    }
};

io.on("connection", (socket) => {
    socket.on("disconnect", () => {
        // ── Persistence: abandon any open attempt for this player
        persist.onPlayerDisconnect(socket.id);
        authorizedHosts.delete(socket.id);
        removePlayerFromSessions(socket.id);
        sessions.forEach((session, code) => {
            if (session.hostSocketId === socket.id) {
                removeSession(code);
                return;
            }
        });
    });

    socket.on("host:authorize", ({ password }, ack = () => { }) => {
        if (typeof password !== "string") {
            return ack({ ok: false, error: "MISSING_PASSWORD" });
        }
        if (password === HOST_SECRET) {
            authorizedHosts.add(socket.id);
            return ack({ ok: true });
        }
        ack({ ok: false, error: "INVALID_PASSWORD" });
    });

    socket.on("host:createSession", (payload, ack = () => { }) => {
        if (!authorizedHosts.has(socket.id)) {
            return ack({ ok: false, error: "UNAUTHORIZED" });
        }
        const config = {
            title: safeString(payload.title, "Sesión ISO"),
            context: safeString(payload.context, ""),
            isoFocus: Array.isArray(payload.isoFocus) && payload.isoFocus.length > 0 ? payload.isoFocus : ["ISO 9241"],
            questionCount: Number(payload.questionCount) || 6,
            language: payload.language || "ES",
            source: payload.source || "predefined",
            predefinedGameId: payload.predefinedGameId || null,
            timerSeconds: Number(payload.timerSeconds) || APP_CONFIG.defaultTimerSeconds
        };

        const code = generateSessionCode();
        const session = {
            code,
            hostSocketId: socket.id,
            config,
            status: "pending",
            players: new Map(),
            game: null,
            questionIndex: -1,
            questionOpen: false,
            responses: new Map(),
            createdAt: Date.now(),
            llmError: false
        };
        sessions.set(code, session);
        socket.join(toRoom(code));
        ack({ ok: true, code });
    });

    socket.on("host:attachGame", ({ code, game, llmError = false }, ack = () => { }) => {
        const { session, error } = ensureHost(socket, code);
        if (error) return ack({ ok: false, error });
        if (!game || !Array.isArray(game.questions) || game.questions.length === 0) {
            return ack({ ok: false, error: "INVALID_GAME" });
        }
        // Trim questions to configured count
        const maxQ = session.config.questionCount || game.questions.length;
        if (game.questions.length > maxQ) {
            game.questions = shuffleArray([...game.questions]).slice(0, maxQ);
        }
        session.game = game;
        session.status = "game_ready";
        session.llmError = Boolean(llmError);
        ack({ ok: true, questionCount: game.questions.length });
        io.to(session.hostSocketId).emit("session:gameReady", {
            gameTitle: {
                es: game.game_title_es,
                en: game.game_title_en
            },
            llmError: session.llmError
        });
    });

    socket.on("host:usePredefined", ({ code, gameId }, ack = () => { }) => {
        const { session, error } = ensureHost(socket, code);
        if (error) return ack({ ok: false, error });
        const originalGame = getPredefinedGame(gameId);
        if (!originalGame) return ack({ ok: false, error: "NO_GAME" });
        // Deep-copy so we don't mutate the predefined data
        const game = JSON.parse(JSON.stringify(originalGame));
        // Trim questions to configured count
        const maxQ = session.config.questionCount || game.questions.length;
        if (game.questions.length > maxQ) {
            game.questions = shuffleArray(game.questions).slice(0, maxQ);
        }
        session.game = game;
        session.status = "game_ready";
        session.llmError = false;
        ack({ ok: true, questionCount: game.questions.length, gameId: game.game_id });
        io.to(session.hostSocketId).emit("session:gameReady", {
            gameTitle: {
                es: game.game_title_es,
                en: game.game_title_en
            },
            llmError: false
        });
    });

    socket.on("host:startGame", ({ code }, ack = () => { }) => {
        const { session, error } = ensureHost(socket, code);
        if (error) return ack({ ok: false, error });
        if (!session.game) return ack({ ok: false, error: "NO_GAME" });
        session.status = "ready";
        io.to(toRoom(code)).emit("session:ready", {
            code,
            title: session.config.title,
            context: session.config.context,
            isoFocus: session.config.isoFocus,
            language: session.config.language,
            totalQuestions: session.game.questions.length,
            timerSeconds: session.config.timerSeconds,
            gameTitle: {
                es: session.game.game_title_es,
                en: session.game.game_title_en
            }
        });
        // ── Persistence: create game_attempts for all registered players
        persist.onGameStarted(sessions, code);
        ack({ ok: true });
    });

    socket.on("host:launchQuestion", ({ code }, ack = () => { }) => {
        const { session, error } = ensureHost(socket, code);
        if (error) return ack({ ok: false, error });
        if (!session.game) return ack({ ok: false, error: "NO_GAME" });
        if (session.questionOpen) return ack({ ok: false, error: "QUESTION_IN_PROGRESS" });
        if (session.questionIndex + 1 >= session.game.questions.length) {
            return ack({ ok: false, error: "NO_MORE_QUESTIONS" });
        }
        session.questionIndex += 1;
        const question = getQuestionPayload(session.game.questions[session.questionIndex], session.config.language);
        session.questionOpen = true;
        session.responses.clear();
        session.currentQuestionStart = Date.now();
        io.to(toRoom(code)).emit("question:start", {
            question,
            index: session.questionIndex + 1,
            total: session.game.questions.length,
            timerSeconds: session.config.timerSeconds,
            language: session.config.language
        });
        ack({ ok: true, index: session.questionIndex });
    });

    socket.on("host:closeQuestion", ({ code }, ack = () => { }) => {
        const { session, error } = ensureHost(socket, code);
        if (error) return ack({ ok: false, error });
        if (!session.questionOpen) return ack({ ok: false, error: "NO_ACTIVE_QUESTION" });
        finalizeQuestion(session);
        if (session.questionIndex + 1 === session.game.questions.length) {
            emitFinalAwards(session);
            // ── Persistence: complete all game_attempts
            persist.onGameEnded(sessions, code);
        }
        ack({ ok: true });
    });

    socket.on("host:endGame", ({ code }, ack = () => { }) => {
        const { session, error } = ensureHost(socket, code);
        if (error) return ack({ ok: false, error });
        emitFinalAwards(session);
        // ── Persistence: complete all game_attempts
        persist.onGameEnded(sessions, code);
        session.status = "finished";
        ack({ ok: true });
    });

    socket.on("player:joinSession", ({ code, nickname, userId, university }, ack = () => { }) => {
        removePlayerFromSessions(socket.id);
        const session = sessions.get(code);
        if (!session) return ack({ ok: false, error: "NO_SESSION" });
        if (session.players.size >= APP_CONFIG.maxPlayers) {
            return ack({ ok: false, error: "ROOM_FULL" });
        }
        const cleanName = safeString(nickname, "Jugador");
        session.players.set(socket.id, {
            socketId: socket.id,
            nickname: cleanName,
            score: 0,
            correctCount: 0,
            totalTime: 0,
            correctTimeEntries: 0,
            fastestMs: null,
            answers: []
        });
        socket.join(toRoom(code));
        // ── Persistence: track this player's userId for later attempt creation
        if (userId) {
            persist.trackPlayer(socket.id, userId, university || "");
        }
        ack({ ok: true, language: session.config.language, title: session.config.title });
        publishPlayerList(session);
        io.to(session.hostSocketId).emit("session:status", {
            message: `${cleanName} se ha unido / ${cleanName} joined`
        });
    });

    socket.on("player:submitAnswer", ({ code, questionId, choice }, ack = () => { }) => {
        const session = sessions.get(code);
        if (!session || !session.questionOpen || !session.game) {
            return ack({ ok: false, error: "NOT_AVAILABLE" });
        }
        const question = session.game.questions[session.questionIndex];
        if (!question || question.id !== questionId) {
            return ack({ ok: false, error: "NOT_ALLOWED" });
        }
        if (session.responses.has(socket.id)) {
            return ack({ ok: false, error: "ALREADY_ANSWERED" });
        }
        const player = session.players.get(socket.id);
        if (!player) return ack({ ok: false, error: "NO_PLAYER" });

        const timeMs = Date.now() - session.currentQuestionStart;
        const isCorrect = Number(choice) === question.correct_index;
        const timerSeconds = session.config.timerSeconds || APP_CONFIG.defaultTimerSeconds;
        const timeSeconds = timeMs / 1000;
        const timeRatio = Math.max(0, Math.min(1, (timerSeconds - timeSeconds) / timerSeconds));
        let points = 0;
        if (isCorrect) {
            const bonus = Math.round(500 * timeRatio);
            points = 1000 + bonus;
            player.correctCount += 1;
            player.totalTime += timeSeconds;
            player.correctTimeEntries += 1;
            if (player.fastestMs === null || timeSeconds < player.fastestMs) {
                player.fastestMs = timeSeconds;
            }
        }
        player.score += points;
        player.answers.push({ questionId, choice: Number(choice), correct: isCorrect, points, timeSeconds });
        session.responses.set(socket.id, { choice, correct: isCorrect, points, timeMs });
        ack({ ok: true, correct: isCorrect, points });
    });
});

// ── REST API Routes ─────────────────────────────────────

// POST /api/players — Register or lookup player
app.post("/api/players", async (req, res) => {
    try {
        const { nickname, university } = req.body;
        if (!nickname || !university) {
            return res.status(400).json({ error: "nickname and university are required" });
        }
        const result = await persist.ensurePlayer(nickname.trim(), university.trim());
        res.json({ ok: true, userId: result.userId, profileId: result.profileId });
    } catch (err) {
        console.error("[api/players]", err.message);
        res.status(500).json({ error: "Internal server error" });
    }
});

// GET /api/leaderboard?game_key=ISO_KAHOOT
app.get("/api/leaderboard", async (req, res) => {
    try {
        const gameKey = req.query.game_key || "ISO_KAHOOT";
        const limit = Math.min(Number(req.query.limit) || 50, 100);
        const { rows } = await pool.query(
            `SELECT DISTINCT ON (ga.user_id)
                ga.id, ga.user_id, ga.score, ga.correct_count,
                ga.incorrect_count, ga.duration_ms, ga.nickname_snapshot,
                ga.university_snapshot, ga.metadata, ga.completed_at
             FROM game_attempts ga
             WHERE ga.game_key = $1 AND ga.status = 'COMPLETED'
             ORDER BY ga.user_id, ga.score DESC, ga.duration_ms ASC
             LIMIT $2`,
            [gameKey, limit]
        );
        // Re-sort by score descending
        rows.sort((a, b) => b.score - a.score || (a.duration_ms || 0) - (b.duration_ms || 0));
        res.json({ ok: true, leaderboard: rows });
    } catch (err) {
        console.error("[api/leaderboard]", err.message);
        res.status(500).json({ error: "Internal server error" });
    }
});

httpServer.listen(PORT, () => {
    console.log(`ISO Kahoot server listening on http://localhost:${PORT}`);
});
