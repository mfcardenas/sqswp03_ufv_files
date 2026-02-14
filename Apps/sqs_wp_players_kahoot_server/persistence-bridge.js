/**
 * persistence-bridge.js
 * ---------------------
 * Server-side module that persists every player's game attempt
 * in PostgreSQL. Exports functions that server.js calls directly
 * at the appropriate lifecycle moments.
 *
 * Usage (in server.js):
 *   const persist = require("./persistence-bridge");
 *   // When player joins:  persist.trackPlayer(socketId, userId, university)
 *   // When game starts:   await persist.onGameStarted(sessions, code)
 *   // When game ends:     await persist.onGameEnded(sessions, code)
 *   // When player leaves: await persist.onPlayerDisconnect(socketId)
 */

const pool = require("./db");
const crypto = require("crypto");

const GAME_KEY = "ISO_KAHOOT";

/* ── helpers ─────────────────────────────────────────── */

const uuid = () => crypto.randomUUID();

/**
 * Lookup or create user + game_profile.
 * Returns { userId, profileId }.
 */
const ensurePlayer = async (nickname, university) => {
    const client = await pool.connect();
    try {
        await client.query("BEGIN");
        const now = new Date().toISOString();

        // Check existing profile by nickname
        const existing = await client.query(
            `SELECT gp.id AS profile_id, gp.user_id
             FROM game_profiles gp
             WHERE LOWER(gp.nickname) = LOWER($1)
             LIMIT 1`,
            [nickname]
        );

        if (existing.rows.length > 0) {
            await client.query("COMMIT");
            return {
                userId: existing.rows[0].user_id,
                profileId: existing.rows[0].profile_id
            };
        }

        // Create user
        const userId = uuid();
        await client.query(
            `INSERT INTO users (id, created_at, updated_at) VALUES ($1, $2, $2)`,
            [userId, now]
        );

        // Create game_profile
        const profileId = uuid();
        await client.query(
            `INSERT INTO game_profiles (id, user_id, nickname, university, created_at, updated_at)
             VALUES ($1, $2, $3, $4, $5, $5)`,
            [profileId, userId, nickname, university, now]
        );

        await client.query("COMMIT");
        return { userId, profileId };
    } catch (err) {
        await client.query("ROLLBACK");
        throw err;
    } finally {
        client.release();
    }
};

/* ── per-socket persistence data ─────────────────────── */

/**
 * Map: socketId → { userId, nickname, university, attemptId, gameStartedAt, sessionCode }
 */
const playerPersistence = new Map();

/**
 * Register a player's persistence data when they join a session.
 * Called from server.js when player:joinSession includes userId.
 */
const trackPlayer = (socketId, userId, university) => {
    if (!userId) return;
    const existing = playerPersistence.get(socketId) || {};
    playerPersistence.set(socketId, {
        ...existing,
        userId,
        university: university || ""
    });
    console.log(`[persist] Tracking player ${socketId} → userId=${userId}`);
};

/**
 * Called when the host starts the game.
 * Creates a STARTED game_attempt for every tracked player in the session.
 */
const onGameStarted = async (sessions, code) => {
    const session = sessions.get(code);
    if (!session || !session.game) return;

    const totalQuestions = session.game.questions.length;
    const maxScore = totalQuestions * 1500;

    console.log(`[persist] Game started for session ${code}, ${session.players.size} players`);

    for (const [socketId, player] of session.players.entries()) {
        const pData = playerPersistence.get(socketId);
        if (!pData || !pData.userId) {
            console.log(`[persist] Skipping player ${player.nickname} (no userId registered)`);
            continue;
        }

        const attemptId = uuid();
        pData.attemptId = attemptId;
        pData.nickname = player.nickname;
        pData.gameStartedAt = Date.now();
        pData.sessionCode = code;
        playerPersistence.set(socketId, pData);

        try {
            const now = new Date().toISOString();
            await pool.query(
                `INSERT INTO game_attempts
                 (id, user_id, game_key, status, started_at, score, max_score,
                  correct_count, incorrect_count, nickname_snapshot, university_snapshot,
                  metadata, created_at, updated_at)
                 VALUES ($1, $2, $3, 'STARTED', $4, 0, $5, 0, 0, $6, $7, '{}', $4, $4)`,
                [attemptId, pData.userId, GAME_KEY, now, maxScore, player.nickname, pData.university]
            );
            console.log(`[persist] Created attempt ${attemptId} for ${player.nickname}`);
        } catch (err) {
            console.error(`[persist] Error creating attempt for ${player.nickname}:`, err.message);
        }
    }
};

/**
 * Called when the game ends (last question closed or host ends game).
 * Updates all game_attempts to COMPLETED with final scores and metadata.
 */
const onGameEnded = async (sessions, code) => {
    const session = sessions.get(code);
    if (!session) return;

    const totalQuestions = session.game ? session.game.questions.length : 0;
    const maxScore = totalQuestions * 1500;

    // Build simple ranking for position info
    const ranking = Array.from(session.players.values())
        .map(p => ({ socketId: p.socketId, nickname: p.nickname, score: p.score }))
        .sort((a, b) => b.score - a.score);

    console.log(`[persist] Game ended for session ${code}, completing attempts`);

    for (const [socketId, player] of session.players.entries()) {
        const pData = playerPersistence.get(socketId);
        if (!pData || !pData.attemptId) continue;

        const durationMs = Date.now() - (pData.gameStartedAt || Date.now());
        const position = ranking.findIndex(r => r.socketId === socketId) + 1;
        const avgTime = player.correctTimeEntries > 0
            ? player.totalTime / player.correctTimeEntries
            : null;

        // Build a question lookup for enrichment
        const questionMap = new Map();
        if (session.game && session.game.questions) {
            for (const q of session.game.questions) {
                questionMap.set(q.id, q);
            }
        }

        // Determine language for question text
        const lang = (session.config?.language || "EN").toLowerCase();
        const pickText = (q, field) => {
            if (lang === "bi") return q[`${field}_en`] || q[`${field}_es`];
            return q[`${field}_${lang}`] || q[`${field}_en`] || q[`${field}_es`];
        };
        const pickOptions = (q) => {
            if (lang === "bi") return q.options_en || q.options_es;
            return q[`options_${lang}`] || q.options_en || q.options_es;
        };

        // Enrich each answer with full question data
        const enrichedAnswers = (player.answers || []).map(a => {
            const q = questionMap.get(a.questionId);
            if (!q) return a; // fallback: keep raw answer
            return {
                question_id: a.questionId,
                question_text: pickText(q, "question"),
                context: pickText(q, "context"),
                iso_standard: q.iso_standard || null,
                difficulty: q.difficulty || null,
                options: pickOptions(q),
                correct_index: q.correct_index,
                player_choice: typeof a.choice === "number" ? a.choice : null,
                correct: a.correct,
                points: a.points,
                time_seconds: parseFloat(a.timeSeconds?.toFixed(2)) || 0
            };
        });

        const metadata = {
            session_code: code,
            game_id: session.game?.game_id || null,
            game_title: session.game?.game_title_en || session.game?.game_title_es || "",
            host_config: {
                title: session.config?.title || "",
                context: session.config?.context || "",
                iso_focus: session.config?.isoFocus || [],
                language: session.config?.language || "EN",
                source: session.config?.source || "predefined",
                timer_seconds: session.config?.timerSeconds || 30
            },
            total_questions: totalQuestions,
            total_players: session.players.size,
            final_position: position,
            avg_response_time_s: avgTime ? parseFloat(avgTime.toFixed(2)) : null,
            fastest_response_s: player.fastestMs ? parseFloat(player.fastestMs.toFixed(2)) : null,
            answers: enrichedAnswers
        };

        try {
            const now = new Date().toISOString();
            await pool.query(
                `UPDATE game_attempts
                 SET status = 'COMPLETED',
                     completed_at = $2,
                     duration_ms = $3,
                     score = $4,
                     max_score = $5,
                     correct_count = $6,
                     incorrect_count = $7,
                     metadata = $8,
                     updated_at = $2
                 WHERE id = $1`,
                [
                    pData.attemptId, now, durationMs,
                    player.score, maxScore,
                    player.correctCount,
                    totalQuestions - player.correctCount,
                    JSON.stringify(metadata)
                ]
            );
            console.log(`[persist] Completed attempt ${pData.attemptId} for ${player.nickname} (score: ${player.score})`);
        } catch (err) {
            console.error(`[persist] Error completing attempt for ${player.nickname}:`, err.message);
        }

        // Clean up
        playerPersistence.delete(socketId);
    }
};

/**
 * Called when a player disconnects.
 * Marks their attempt as ABANDONED if it was still STARTED.
 */
const onPlayerDisconnect = async (socketId) => {
    const pData = playerPersistence.get(socketId);
    if (!pData || !pData.attemptId) {
        playerPersistence.delete(socketId);
        return;
    }

    try {
        const now = new Date().toISOString();
        await pool.query(
            `UPDATE game_attempts
             SET status = 'ABANDONED', completed_at = $2, updated_at = $2
             WHERE id = $1 AND status = 'STARTED'`,
            [pData.attemptId, now]
        );
        console.log(`[persist] Abandoned attempt ${pData.attemptId} (player disconnected)`);
    } catch (err) {
        console.error("[persist] Error abandoning attempt:", err.message);
    }

    playerPersistence.delete(socketId);
};

module.exports = { ensurePlayer, trackPlayer, onGameStarted, onGameEnded, onPlayerDisconnect };
