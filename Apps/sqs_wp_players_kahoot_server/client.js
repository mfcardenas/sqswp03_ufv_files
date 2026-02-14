(() => {
    const socket = io();

    const dom = {
        hostPanel: document.getElementById("host-panel"),
        playerPanel: document.getElementById("player-panel"),
        hostBtn: document.getElementById("btn-host-mode"),
        playerBtn: document.getElementById("btn-player-mode"),
        hostForm: document.getElementById("host-form"),
        playerForm: document.getElementById("player-form"),
        hostContext: document.getElementById("host-context"),
        sessionCode: document.getElementById("session-code"),
        playerList: document.getElementById("player-list"),
        hostQuestion: document.getElementById("host-question"),
        hostTimer: document.getElementById("host-timer"),
        hostResults: document.getElementById("host-results"),
        hostRanking: document.getElementById("host-ranking"),
        playerStatus: document.getElementById("player-status"),
        playerQuestionCard: document.getElementById("player-question-card"),
        playerQuestion: document.getElementById("player-question"),
        playerOptions: document.getElementById("player-options"),
        playerTimer: document.getElementById("player-timer"),
        playerFeedback: document.getElementById("player-feedback"),
        playerRanking: document.getElementById("player-ranking"),
        predefinedSelect: document.getElementById("predefined-select"),
        btnGenerateLLM: document.getElementById("btn-generate-llm"),
        btnUsePredefined: document.getElementById("btn-use-predefined"),
        btnStartSession: document.getElementById("btn-start-session"),
        btnLaunchQuestion: document.getElementById("btn-launch-question"),
        btnCloseQuestion: document.getElementById("btn-close-question"),
        btnEndSession: document.getElementById("btn-end-session"),
        gameTitlePill: document.getElementById("game-title-pill"),
        llmWarning: document.getElementById("llm-warning-pill"),
        rankingTemplate: document.getElementById("ranking-template"),
        playerQuestionHeading: document.getElementById("player-question"),
        playerTimerBox: document.getElementById("player-timer"),
        hostTimerBox: document.getElementById("host-timer")
    };

    const state = {
        role: "host",
        host: {
            sessionCode: null,
            config: null,
            game: null,
            countdownId: null,
            questionLive: false
        },
        player: {
            sessionCode: null,
            nickname: null,
            language: "ES",
            countdownId: null,
            hasAnswered: false,
            currentQuestion: null
        }
    };

    const text = (es, en, lang = state.host?.config?.language || state.player.language || "ES") => {
        if (lang === "EN") return en;
        if (lang === "BI") return `${es}\n${en}`;
        return es;
    };

    const switchRole = (role) => {
        state.role = role;
        if (role === "host") {
            dom.hostPanel.classList.add("show");
            dom.playerPanel.classList.remove("show");
            dom.hostBtn.classList.add("active");
            dom.playerBtn.classList.remove("active");
        } else {
            dom.playerPanel.classList.add("show");
            dom.hostPanel.classList.remove("show");
            dom.playerBtn.classList.add("active");
            dom.hostBtn.classList.remove("active");
        }
    };

    const populatePredefined = () => {
        if (!window.PREDEFINED_GAMES) return;
        window.PREDEFINED_GAMES.forEach(game => {
            const option = document.createElement("option");
            option.value = game.game_id;
            option.textContent = `${game.game_title_es} / ${game.game_title_en}`;
            dom.predefinedSelect.appendChild(option);
        });
    };

    const setHostStatus = (message, type = "info") => {
        dom.hostResults.innerHTML = `<p class="${type}">${message}</p>`;
    };

    const setPlayerStatus = (message, type = "info") => {
        dom.playerStatus.innerHTML = `<span class="${type}">${message}</span>`;
    };

    const renderRanking = (container, ranking) => {
        if (!ranking || ranking.length === 0) {
            container.innerHTML = "";
            return;
        }
        const clone = dom.rankingTemplate.content.cloneNode(true);
        const list = clone.querySelector("ol");
        ranking.slice(0, 10).forEach((entry, idx) => {
            const li = document.createElement("li");
            const avg = entry.avgTime ? `${entry.avgTime.toFixed(1)}s` : "--";
            li.textContent = `${idx + 1}. ${entry.nickname} · ${entry.score} pts · ⏱️ ${avg}`;
            list.appendChild(li);
        });
        container.innerHTML = "";
        container.appendChild(clone);
    };

    const stopCountdown = (key) => {
        if (state[key].countdownId) {
            clearInterval(state[key].countdownId);
            state[key].countdownId = null;
        }
    };

    const startCountdown = (seconds, target, ownerKey) => {
        stopCountdown(ownerKey);
        let remaining = seconds;
        target.textContent = remaining.toString().padStart(2, "0");
        state[ownerKey].countdownId = setInterval(() => {
            remaining -= 1;
            target.textContent = remaining.toString().padStart(2, "0");
            if (remaining <= 0) {
                stopCountdown(ownerKey);
            }
        }, 1000);
    };

    const formatQuestionHTML = (payload, language) => {
        const ctx = language === "EN" ? payload.context.en : payload.context.es;
        const ctxBi = language === "BI" ? `<p>${payload.context.es}</p><p class="muted">${payload.context.en}</p>` : `<p>${ctx}</p>`;
        const q = language === "EN" ? payload.question.en : payload.question.es;
        const qBi = language === "BI" ? `<h3>${payload.question.es}</h3><p class="muted">${payload.question.en}</p>` : `<h3>${q}</h3>`;
        return `${ctxBi}${qBi}<p class="tag">${payload.iso_standard} · ${payload.difficulty}</p>`;
    };

    const renderOptions = (payload, language) => {
        const options = language === "EN" ? payload.options.en : payload.options.es;
        const optionsBi = payload.options;
        dom.playerOptions.innerHTML = "";
        options.forEach((label, idx) => {
            const btn = document.createElement("button");
            btn.type = "button";
            btn.dataset.index = idx;
            if (language === "BI") {
                btn.innerHTML = `<strong>${optionsBi.es[idx]}</strong><br><span class="muted">${optionsBi.en[idx]}</span>`;
            } else {
                btn.textContent = label;
            }
            btn.addEventListener("click", () => handlePlayerAnswer(idx));
            dom.playerOptions.appendChild(btn);
        });
    };

    const getSessionConfigFromForm = () => {
        const formData = new FormData(dom.hostForm);
        const isoFocus = formData.getAll("isoFocus");
        return {
            title: formData.get("title") || "Sesión ISO",
            context: formData.get("context") || "",
            isoFocus,
            questionCount: Number(formData.get("questionCount")) || 6,
            language: formData.get("language") || "ES",
            source: formData.get("source") || "predefined",
            predefinedGameId: formData.get("predefinedGame"),
            timerSeconds: Number(formData.get("timerSeconds")) || APP_CONFIG.defaultTimerSeconds
        };
    };

    const createSession = (config) => {
        socket.emit("host:createSession", config, (res) => {
            if (!res?.ok) {
                setHostStatus("No se pudo crear la sesión.");
                return;
            }
            state.host.game = null;
            state.host.questionLive = false;
            state.host.sessionCode = res.code;
            state.host.config = config;
            dom.sessionCode.textContent = `Código: ${res.code}`;
            dom.hostContext.textContent = config.context;
            setHostStatus("Sesión creada. Elige fuente de preguntas.");
            dom.btnGenerateLLM.disabled = config.source !== "llm";
            dom.btnUsePredefined.disabled = false;
            dom.btnEndSession.disabled = false;
            dom.btnStartSession.disabled = true;
            dom.btnLaunchQuestion.disabled = true;
            dom.btnCloseQuestion.disabled = true;
            dom.gameTitlePill.textContent = "Juego no cargado";
            dom.llmWarning.hidden = true;
            dom.hostRanking.innerHTML = "";
        });
    };

    const attachPredefinedGame = () => {
        if (!state.host.sessionCode) {
            setHostStatus("Crea la sesión primero.");
            return;
        }
        const gameId = dom.predefinedSelect.value;
        socket.emit("host:usePredefined", { code: state.host.sessionCode, gameId }, (res) => {
            if (!res?.ok) {
                setHostStatus("No se pudo cargar el juego predefinido.", "error");
                return;
            }
            const game = window.PREDEFINED_GAMES.find(g => g.game_id === res.gameId) || window.PREDEFINED_GAMES[0];
            state.host.game = game;
            dom.gameTitlePill.textContent = `${game.game_title_es} / ${game.game_title_en}`;
            dom.llmWarning.hidden = true;
            dom.btnStartSession.disabled = false;
            setHostStatus("Juego predefinido listo. Puedes iniciar la partida.", "success");
        });
    };

    const buildLLMPrompt = (config) => {
        const isoList = config.isoFocus.join(", ");
        return `Genera un objeto JSON con la estructura de juego ISO descrita (game_title_es, game_title_en, iso_focus, questions).` +
            ` Debe contener ${config.questionCount} preguntas sobre ${isoList}.` +
            ` Cada pregunta incluye: context_es, context_en, question_es, question_en, options_es (4), options_en (4), correct_index, explanation_es, explanation_en, iso_standard, difficulty.` +
            ` Usa escenarios realistas en proyectos de software. Contexto docente: ${config.context || "Sin contexto"}.` +
            ` Responde solo con JSON válido.`;
    };

    const generateQuizFromLLM = async (config) => {
        if (!window.LLM_CONFIG?.enabled) {
            throw new Error("LLM_DISABLED");
        }
        const controller = new AbortController();
        const timeout = setTimeout(() => controller.abort(), window.LLM_CONFIG.timeoutMs);
        const prompt = buildLLMPrompt(config);
        try {
            const response = await fetch(window.LLM_CONFIG.baseUrl, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ model: window.LLM_CONFIG.model, prompt, stream: false }),
                signal: controller.signal
            });
            clearTimeout(timeout);
            if (!response.ok) {
                throw new Error(`HTTP ${response.status}`);
            }
            const text = await response.text();
            try {
                return JSON.parse(text);
            } catch (err) {
                const match = text.match(/\{[\s\S]*\}/);
                if (match) {
                    return JSON.parse(match[0]);
                }
                throw err;
            }
        } catch (error) {
            clearTimeout(timeout);
            throw error;
        }
    };

    const attachLLMGame = async () => {
        if (!state.host.sessionCode) {
            setHostStatus("Crea la sesión antes de llamar al LLM.", "warning");
            return;
        }
        const config = state.host.config;
        setHostStatus("Generando preguntas con IA / Generating quiz via LLM...");
        try {
            const game = await generateQuizFromLLM(config);
            socket.emit("host:attachGame", { code: state.host.sessionCode, game, llmError: false }, (res) => {
                if (!res?.ok) {
                    setHostStatus("El juego generado no es válido.", "error");
                    return;
                }
                state.host.game = game;
                dom.gameTitlePill.textContent = `${game.game_title_es} / ${game.game_title_en}`;
                dom.llmWarning.hidden = true;
                dom.btnStartSession.disabled = false;
                setHostStatus("Juego generado con IA listo.", "success");
            });
        } catch (error) {
            dom.llmWarning.hidden = false;
            setHostStatus("IA no disponible, usando juego predefinido.", "warning");
            socket.emit("host:usePredefined", { code: state.host.sessionCode }, (res) => {
                if (res?.ok) {
                    const game = window.PREDEFINED_GAMES.find(g => g.game_id === res.gameId) || window.PREDEFINED_GAMES[0];
                    state.host.game = game;
                    dom.gameTitlePill.textContent = `${game.game_title_es} / ${game.game_title_en}`;
                    dom.btnStartSession.disabled = false;
                }
            });
        }
    };

    const handlePlayerAnswer = (choice) => {
        if (state.player.hasAnswered) return;
        const question = state.player.currentQuestion;
        if (!question) return;
        state.player.hasAnswered = true;
        dom.playerOptions.querySelectorAll("button").forEach(btn => btn.disabled = true);
        socket.emit("player:submitAnswer", {
            code: state.player.sessionCode,
            questionId: question.id,
            choice
        });
    };

    const updateHostButtons = () => {
        dom.btnLaunchQuestion.disabled = !state.host.game;
        dom.btnCloseQuestion.disabled = !state.host.questionLive;
    };

    const onQuestionStart = (payload) => {
        const { question, index, total, timerSeconds, language } = payload;
        state.player.currentQuestion = question;
        state.host.questionLive = true;
        dom.hostQuestion.innerHTML = `<h3>Pregunta ${index}/${total}</h3>${formatQuestionHTML(question, language)}`;
        startCountdown(timerSeconds, dom.hostTimer, "host");
        updateHostButtons();
        if (state.role === "player" && state.player.sessionCode) {
            dom.playerQuestionCard.hidden = false;
            state.player.hasAnswered = false;
            dom.playerFeedback.textContent = "";
            dom.playerQuestion.innerHTML = formatQuestionHTML(question, language);
            renderOptions(question, language);
            startCountdown(timerSeconds, dom.playerTimer, "player");
        }
    };

    const onQuestionResults = (payload) => {
        const { stats, explanation, rankingTop } = payload;
        const lang = state.host.config?.language || "ES";
        dom.hostResults.innerHTML = `
            <p><strong>${text("Respuesta correcta","Correct answer", lang)}</strong>: ${text(explanation.es, explanation.en, lang)}</p>
            <p>${text("Aciertos","Correct")}: ${stats.correct} | ${text("Errores","Wrong")}: ${stats.incorrect}</p>
        `;
        renderRanking(dom.hostRanking, rankingTop);
        state.host.questionLive = false;
        updateHostButtons();
        stopCountdown("host");
    };

    const onPlayerFeedback = (payload) => {
        const lang = state.player.language;
        const message = payload.correct
            ? text("✅ ¡Respuesta correcta!", "✅ Correct answer!", lang)
            : text("❌ Respuesta incorrecta", "❌ Incorrect answer", lang);
        dom.playerFeedback.textContent = `${message} · ${payload.points} pts`;
        dom.playerFeedback.className = `feedback ${payload.correct ? "correct" : "incorrect"}`;
        stopCountdown("player");
    };

    const onRankingUpdate = ({ ranking }) => {
        renderRanking(dom.hostRanking, ranking);
        if (state.role === "player") {
            renderRanking(dom.playerRanking, ranking);
        }
    };

    const onFinalAwards = ({ ranking, awards }) => {
        const lang = state.host.config?.language || state.player.language;
        const top = awards.topScorer ? `${awards.topScorer.nickname} · ${awards.topScorer.score} pts` : text("Sin datos", "No data", lang);
        const fast = awards.fastest ? `${awards.fastest.nickname} (${awards.fastest.fastestMs?.toFixed(1)}s)` : text("Sin ganador veloz", "No fastest player", lang);
        const html = `
            <h3>${text("Ranking final","Final ranking", lang)}</h3>
            <p>${text("Máxima puntuación","Top scorer", lang)}: ${top}</p>
            <p>${text("Más rápido (>=50% aciertos)", "Fastest (>=50% correct)", lang)}: ${fast}</p>
        `;
        dom.hostResults.innerHTML = html;
        renderRanking(dom.hostRanking, ranking);
        if (state.role === "player") {
            dom.playerFeedback.innerHTML = html;
        }
    };

    dom.hostBtn.addEventListener("click", () => switchRole("host"));
    dom.playerBtn.addEventListener("click", () => switchRole("player"));

    dom.hostForm.addEventListener("submit", (event) => {
        event.preventDefault();
        const config = getSessionConfigFromForm();
        createSession(config);
    });

    dom.hostForm.querySelectorAll('input[name="source"]').forEach(radio => {
        radio.addEventListener('change', () => {
            const useLLM = radio.value === 'llm' && radio.checked;
            dom.btnGenerateLLM.disabled = !useLLM;
        });
    });

    dom.btnUsePredefined.addEventListener("click", attachPredefinedGame);
    dom.btnGenerateLLM.addEventListener("click", attachLLMGame);

    dom.btnStartSession.addEventListener("click", () => {
        if (!state.host.sessionCode || !state.host.game) return;
        socket.emit("host:startGame", { code: state.host.sessionCode }, (res) => {
            if (!res?.ok) {
                setHostStatus("No se pudo iniciar la partida.", "error");
                return;
            }
            dom.btnStartSession.disabled = true;
            dom.btnLaunchQuestion.disabled = false;
            setHostStatus("Partida lista. Lanza la primera pregunta cuando estés listo.", "success");
        });
    });

    dom.btnLaunchQuestion.addEventListener("click", () => {
        if (!state.host.sessionCode) return;
        socket.emit("host:launchQuestion", { code: state.host.sessionCode }, (res) => {
            if (!res?.ok) {
                setHostStatus(text("No hay más preguntas","No more questions", state.host.config?.language), "warning");
                return;
            }
            dom.btnCloseQuestion.disabled = false;
        });
    });

    dom.btnCloseQuestion.addEventListener("click", () => {
        if (!state.host.sessionCode) return;
        socket.emit("host:closeQuestion", { code: state.host.sessionCode });
        dom.btnCloseQuestion.disabled = true;
    });

    dom.btnEndSession.addEventListener("click", () => {
        if (!state.host.sessionCode) return;
        socket.emit("host:endGame", { code: state.host.sessionCode });
    });

    dom.playerForm.addEventListener("submit", (event) => {
        event.preventDefault();
        const formData = new FormData(dom.playerForm);
        const nickname = formData.get("nickname");
        const code = (formData.get("sessionCode") || "").trim().toUpperCase();
        socket.emit("player:joinSession", { nickname, code }, (res) => {
            if (!res?.ok) {
                setPlayerStatus("El código no existe / Session code not found", "error");
                return;
            }
            state.player.sessionCode = code;
            state.player.nickname = nickname;
            state.player.language = res.language;
            setPlayerStatus(text("Esperando al docente","Waiting for host", res.language));
            dom.playerQuestionCard.hidden = false;
        });
    });

    socket.on("session:players", ({ players }) => {
        dom.playerList.innerHTML = players.map(p => `<li>${p.nickname} (${p.score} pts)</li>`).join("");
    });

    socket.on("session:gameReady", ({ gameTitle, llmError }) => {
        dom.gameTitlePill.textContent = `${gameTitle.es} / ${gameTitle.en}`;
        dom.llmWarning.hidden = !llmError;
        if (!llmError) {
            setHostStatus(text("Juego listo","Game ready", state.host.config?.language), "success");
        } else {
            setHostStatus(text("LLM no disponible, usando reserva","LLM offline, using fallback", state.host.config?.language), "warning");
        }
    });

    socket.on("session:ready", (payload) => {
        const lang = payload.language;
        state.player.language = state.player.language || lang;
        setHostStatus(text("Participantes listos","Players ready", lang));
        if (state.role === "player") {
            setPlayerStatus(text("La partida inicia pronto","Game starts soon", lang));
        }
    });

    socket.on("question:start", onQuestionStart);
    socket.on("question:results", onQuestionResults);
    socket.on("question:feedback", onPlayerFeedback);
    socket.on("session:ranking", onRankingUpdate);
    socket.on("session:final", onFinalAwards);

    socket.on("session:ended", () => {
        setHostStatus("Sesión finalizada / Session ended", "warning");
        setPlayerStatus("Sesión finalizada / Session ended", "warning");
        stopCountdown("host");
        stopCountdown("player");
    });

    socket.on("session:status", ({ message }) => {
        setHostStatus(message, "info");
    });

    populatePredefined();
})();
