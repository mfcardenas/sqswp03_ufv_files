(() => {
    const socket = io();

    const dom = {
        hostLock: document.getElementById("host-lock"),
        hostPanel: document.getElementById("host-panel"),
        hostAuthForm: document.getElementById("host-auth-form"),
        hostAuthStatus: document.getElementById("host-auth-status"),
        hostForm: document.getElementById("host-form"),
        sessionCode: document.getElementById("session-code"),
        hostContext: document.getElementById("host-context"),
        playerList: document.getElementById("player-list"),
        gameTitlePill: document.getElementById("game-title-pill"),
        llmWarning: document.getElementById("llm-warning-pill"),
        btnGenerateLLM: document.getElementById("btn-generate-llm"),
        btnUsePredefined: document.getElementById("btn-use-predefined"),
        btnStartSession: document.getElementById("btn-start-session"),
        btnLaunchQuestion: document.getElementById("btn-launch-question"),
        btnCloseQuestion: document.getElementById("btn-close-question"),
        btnEndSession: document.getElementById("btn-end-session"),
        hostQuestion: document.getElementById("host-question"),
        hostTimer: document.getElementById("host-timer"),
        hostResults: document.getElementById("host-results"),
        hostRanking: document.getElementById("host-ranking"),
        predefinedSelect: document.getElementById("predefined-select"),
        rankingTemplate: document.getElementById("ranking-template"),
        hostPasswordHint: document.getElementById("host-password-hint"),
        languageSelect: document.querySelector("select[name='language']")
    };

    const uiLang = document.body?.dataset?.uiLang === "en" ? "en" : "es";
    const LOCAL_STORAGE_LANG_KEY = "isoQuizPreferredLanguage";
    const UI_TEXT = {
        es: {
            passwordHintLabel: "Tip",
            authExpired: "Sesión caducada. Introduce de nuevo la contraseña.",
            authNeeded: "Debes desbloquear el panel antes de continuar.",
            authWrong: "Contraseña incorrecta.",
            sessionCreateError: "No se pudo crear la sesión.",
            sessionCreated: "Sesión creada. Elige fuente de preguntas.",
            gameNotLoaded: "Juego no cargado",
            createFirstWarning: "Crea la sesión primero.",
            predefinedLoadError: "No se pudo cargar el juego predefinido.",
            predefinedReady: "Juego predefinido listo.",
            llmNeedsSession: "Crea la sesión antes de llamar al LLM.",
            llmGenerating: "Generando preguntas con IA...",
            llmInvalidGame: "El juego generado no es válido.",
            llmFallback: "IA no disponible, usando juego predefinido.",
            startGameError: "No se pudo iniciar la partida.",
            gamePrimed: "Partida lista. Lanza la primera pregunta cuando estés listo.",
            noMoreQuestions: "No hay más preguntas.",
            startConfigHint: "Introduce la configuración de tu sesión.",
            gameReady: "Juego listo",
            llmFallbackShort: "LLM no disponible, usando reserva",
            playersReady: "Participantes listos",
            sessionEnded: "Sesión finalizada",
            rankingTitle: "Ranking",
            questionLabel: "Pregunta"
        },
        en: {
            passwordHintLabel: "Hint",
            authExpired: "Session expired. Please re-enter the password.",
            authNeeded: "Unlock the host panel before continuing.",
            authWrong: "Incorrect password.",
            sessionCreateError: "Could not create the session.",
            sessionCreated: "Session ready. Choose the question source.",
            gameNotLoaded: "Game not loaded",
            createFirstWarning: "Create the session first.",
            predefinedLoadError: "Could not load the predefined game.",
            predefinedReady: "Predefined game ready.",
            llmNeedsSession: "Create the session before requesting the AI.",
            llmGenerating: "Generating quiz via AI...",
            llmInvalidGame: "The generated game is invalid.",
            llmFallback: "AI unavailable, loading a predefined game.",
            startGameError: "Could not start the match.",
            gamePrimed: "Match ready. Launch the first question whenever you want.",
            noMoreQuestions: "No more questions available.",
            startConfigHint: "Fill in your session details to begin.",
            gameReady: "Game ready",
            llmFallbackShort: "LLM offline, using fallback",
            playersReady: "Players ready",
            sessionEnded: "Session ended",
            rankingTitle: "Leaderboard",
            questionLabel: "Question"
        }
    };

    const ui = (key) => UI_TEXT[uiLang]?.[key] || key;

    const state = {
        authorized: false,
        sessionCode: null,
        config: null,
        game: null,
        countdownId: null,
        questionLive: false
    };

    const currentLang = () => state.config?.language || "ES";

    const text = (es, en) => {
        const lang = currentLang();
        if (lang === "EN") return en;
        if (lang === "BI") return `${es}\n${en}`;
        return es;
    };

    const populatePredefined = () => {
        if (!window.PREDEFINED_GAMES) return;
        dom.predefinedSelect.innerHTML = "";
        window.PREDEFINED_GAMES.forEach(game => {
            const option = document.createElement("option");
            option.value = game.game_id;
            option.textContent = `${game.game_title_es} / ${game.game_title_en}`;
            dom.predefinedSelect.appendChild(option);
        });
    };

    const applyPasswordHint = () => {
        if (dom.hostPasswordHint && window.APP_CONFIG?.hostPasswordHint) {
            dom.hostPasswordHint.textContent = `${ui("passwordHintLabel")}: ${window.APP_CONFIG.hostPasswordHint}`;
        }
    };

    const readPreferredLanguage = () => {
        try {
            return window.localStorage?.getItem(LOCAL_STORAGE_LANG_KEY) || null;
        } catch (err) {
            return null;
        }
    };

    const writePreferredLanguage = (lang) => {
        try {
            if (lang) {
                window.localStorage?.setItem(LOCAL_STORAGE_LANG_KEY, lang);
            }
        } catch (err) {
            /* ignore storage errors */
        }
    };

    const applyLanguagePreference = () => {
        if (!dom.languageSelect) return;
        const stored = readPreferredLanguage();
        const fallback = uiLang === "en" ? "EN" : "ES";
        const target = stored || fallback;
        dom.languageSelect.value = target;
    };

    const togglePanels = (authorized) => {
        state.authorized = authorized;
        if (authorized) {
            dom.hostLock?.classList.remove("show");
            dom.hostPanel?.classList.add("show");
            dom.hostAuthStatus.textContent = "";
        } else {
            dom.hostPanel?.classList.remove("show");
            dom.hostLock?.classList.add("show");
        }
    };

    const setAuthStatus = (message, type = "info") => {
        if (!dom.hostAuthStatus) return;
        dom.hostAuthStatus.textContent = message;
        dom.hostAuthStatus.className = `status ${type}`;
    };

    const handleUnauthorized = () => {
        togglePanels(false);
        setAuthStatus(ui("authExpired"), "error");
    };

    const guardAuthorized = () => {
        if (state.authorized) return true;
        setAuthStatus(ui("authNeeded"), "warning");
        return false;
    };

    const setHostStatus = (message, type = "info") => {
        dom.hostResults.innerHTML = `<p class="${type}">${message}</p>`;
    };

    const renderRanking = (container, ranking) => {
        if (!ranking || ranking.length === 0) {
            container.innerHTML = "";
            return;
        }
        const clone = dom.rankingTemplate.content.cloneNode(true);
        const heading = clone.querySelector("h3");
        if (heading) heading.textContent = ui("rankingTitle");
        const list = clone.querySelector("ol");
        ranking.slice(0, 10).forEach((entry, idx) => {
            const avg = entry.avgTime ? `${entry.avgTime.toFixed(1)}s` : "--";
            list.insertAdjacentHTML("beforeend", `<li>${idx + 1}. ${entry.nickname} · ${entry.score} pts · ⏱️ ${avg}</li>`);
        });
        container.innerHTML = "";
        container.appendChild(clone);
    };

    const stopCountdown = () => {
        if (state.countdownId) {
            clearInterval(state.countdownId);
            state.countdownId = null;
        }
    };

    const startCountdown = (seconds) => {
        stopCountdown();
        let remaining = seconds;
        dom.hostTimer.textContent = remaining.toString().padStart(2, "0");
        state.countdownId = setInterval(() => {
            remaining -= 1;
            dom.hostTimer.textContent = remaining.toString().padStart(2, "0");
            if (remaining <= 0) {
                stopCountdown();
            }
        }, 1000);
    };

    const formatQuestionHTML = (payload) => {
        const language = currentLang();
        const ctx = language === "EN" ? payload.context.en : payload.context.es;
        const ctxBi = language === "BI" ? `<p>${payload.context.es}</p><p class="muted">${payload.context.en}</p>` : `<p>${ctx}</p>`;
        const q = language === "EN" ? payload.question.en : payload.question.es;
        const qBi = language === "BI" ? `<h3>${payload.question.es}</h3><p class="muted">${payload.question.en}</p>` : `<h3>${q}</h3>`;
        return `${ctxBi}${qBi}<p class="tag">${payload.iso_standard} · ${payload.difficulty}</p>`;
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
        if (!guardAuthorized()) return;
        socket.emit("host:createSession", config, (res) => {
            if (!res?.ok) {
                if (res?.error === "UNAUTHORIZED") {
                    handleUnauthorized();
                }
                setHostStatus(ui("sessionCreateError"));
                return;
            }
            state.sessionCode = res.code;
            state.config = config;
            state.game = null;
            state.questionLive = false;
            dom.sessionCode.textContent = `Código: ${res.code}`;
            dom.hostContext.textContent = config.context;
            dom.gameTitlePill.textContent = ui("gameNotLoaded");
            dom.llmWarning.hidden = true;
            dom.hostRanking.innerHTML = "";
            dom.btnUsePredefined.disabled = false;
            dom.btnGenerateLLM.disabled = config.source !== "llm";
            dom.btnEndSession.disabled = false;
            dom.btnStartSession.disabled = true;
            dom.btnLaunchQuestion.disabled = true;
            dom.btnCloseQuestion.disabled = true;
            writePreferredLanguage(state.config.language);
            setHostStatus(ui("sessionCreated"));
        });
    };

    const attachPredefinedGame = () => {
        if (!state.sessionCode) {
            setHostStatus(ui("createFirstWarning"), "warning");
            return;
        }
        const gameId = dom.predefinedSelect.value;
        socket.emit("host:usePredefined", { code: state.sessionCode, gameId }, (res) => {
            if (!res?.ok) {
                if (res?.error === "UNAUTHORIZED") {
                    handleUnauthorized();
                }
                setHostStatus(ui("predefinedLoadError"), "error");
                return;
            }
            const game = window.PREDEFINED_GAMES.find(g => g.game_id === res.gameId) || window.PREDEFINED_GAMES[0];
            state.game = game;
            dom.gameTitlePill.textContent = `${game.game_title_es} / ${game.game_title_en}`;
            dom.llmWarning.hidden = true;
            dom.btnStartSession.disabled = false;
            setHostStatus(ui("predefinedReady"), "success");
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
            const body = await response.text();
            try {
                return JSON.parse(body);
            } catch (err) {
                const match = body.match(/\{[\s\S]*\}/);
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
        if (!state.sessionCode) {
            setHostStatus(ui("llmNeedsSession"), "warning");
            return;
        }
        setHostStatus(ui("llmGenerating"));
        try {
            const game = await generateQuizFromLLM(state.config);
            socket.emit("host:attachGame", { code: state.sessionCode, game, llmError: false }, (res) => {
                if (!res?.ok) {
                    if (res?.error === "UNAUTHORIZED") {
                        handleUnauthorized();
                    }
                    setHostStatus(ui("llmInvalidGame"), "error");
                    return;
                }
                state.game = game;
                dom.gameTitlePill.textContent = `${game.game_title_es} / ${game.game_title_en}`;
                dom.llmWarning.hidden = true;
                dom.btnStartSession.disabled = false;
                setHostStatus(ui("gameReady"), "success");
            });
        } catch (error) {
            dom.llmWarning.hidden = false;
            setHostStatus(ui("llmFallback"), "warning");
            socket.emit("host:usePredefined", { code: state.sessionCode }, (res) => {
                if (res?.ok) {
                    const game = window.PREDEFINED_GAMES.find(g => g.game_id === res.gameId) || window.PREDEFINED_GAMES[0];
                    state.game = game;
                    dom.gameTitlePill.textContent = `${game.game_title_es} / ${game.game_title_en}`;
                    dom.btnStartSession.disabled = false;
                }
            });
        }
    };

    const updateHostButtons = () => {
        dom.btnLaunchQuestion.disabled = !state.game;
        dom.btnCloseQuestion.disabled = !state.questionLive;
    };

    const onQuestionStart = ({ question, index, total, timerSeconds }) => {
        state.questionLive = true;
        dom.hostQuestion.innerHTML = `<h3>${ui("questionLabel")} ${index}/${total}</h3>${formatQuestionHTML(question)}`;
        startCountdown(timerSeconds);
        updateHostButtons();
    };

    const onQuestionResults = ({ stats, explanation, rankingTop }) => {
        dom.hostResults.innerHTML = `
            <p><strong>${text("Respuesta correcta","Correct answer")}</strong>: ${text(explanation.es, explanation.en)}</p>
            <p>${text("Aciertos","Correct")}: ${stats.correct} | ${text("Errores","Wrong")}: ${stats.incorrect}</p>
        `;
        renderRanking(dom.hostRanking, rankingTop);
        state.questionLive = false;
        updateHostButtons();
        stopCountdown();
    };

    const onRankingUpdate = ({ ranking }) => {
        renderRanking(dom.hostRanking, ranking);
    };

    const onFinalAwards = ({ ranking, awards }) => {
        const top = awards.topScorer ? `${awards.topScorer.nickname} · ${awards.topScorer.score} pts` : text("Sin datos", "No data");
        const fast = awards.fastest ? `${awards.fastest.nickname} (${awards.fastest.fastestMs?.toFixed(1)}s)` : text("Sin ganador veloz", "No fastest player");
        dom.hostResults.innerHTML = `
            <h3>${text("Ranking final","Final ranking")}</h3>
            <p>${text("Máxima puntuación","Top scorer")}: ${top}</p>
            <p>${text("Más rápido (>=50% aciertos)", "Fastest (>=50% correct)")}: ${fast}</p>
        `;
        renderRanking(dom.hostRanking, ranking);
    };

    dom.hostForm.addEventListener("submit", (event) => {
        event.preventDefault();
        const config = getSessionConfigFromForm();
        createSession(config);
    });

    dom.hostForm.querySelectorAll('input[name="source"]').forEach(radio => {
        radio.addEventListener('change', () => {
            dom.btnGenerateLLM.disabled = !(radio.value === 'llm' && radio.checked);
        });
    });

    if (dom.languageSelect) {
        dom.languageSelect.addEventListener("change", () => {
            const newLang = dom.languageSelect.value;
            writePreferredLanguage(newLang);
        });
    }

    dom.btnUsePredefined.addEventListener("click", attachPredefinedGame);
    dom.btnGenerateLLM.addEventListener("click", attachLLMGame);

    dom.btnStartSession.addEventListener("click", () => {
        if (!state.sessionCode || !state.game) return;
        socket.emit("host:startGame", { code: state.sessionCode }, (res) => {
            if (!res?.ok) {
                if (res?.error === "UNAUTHORIZED") {
                    handleUnauthorized();
                }
                setHostStatus(ui("startGameError"), "error");
                return;
            }
            dom.btnStartSession.disabled = true;
            dom.btnLaunchQuestion.disabled = false;
            setHostStatus(ui("gamePrimed"), "success");
        });
    });

    dom.btnLaunchQuestion.addEventListener("click", () => {
        if (!state.sessionCode) return;
        socket.emit("host:launchQuestion", { code: state.sessionCode }, (res) => {
            if (!res?.ok) {
                if (res?.error === "UNAUTHORIZED") {
                    handleUnauthorized();
                }
                setHostStatus(ui("noMoreQuestions"), "warning");
                return;
            }
            dom.btnCloseQuestion.disabled = false;
        });
    });

    dom.btnCloseQuestion.addEventListener("click", () => {
        if (!state.sessionCode) return;
        socket.emit("host:closeQuestion", { code: state.sessionCode }, (res) => {
            if (res?.error === "UNAUTHORIZED") {
                handleUnauthorized();
                return;
            }
            dom.btnCloseQuestion.disabled = true;
        });
    });

    dom.btnEndSession.addEventListener("click", () => {
        if (!state.sessionCode) return;
        socket.emit("host:endGame", { code: state.sessionCode }, (res) => {
            if (res?.error === "UNAUTHORIZED") {
                handleUnauthorized();
            }
        });
    });

    if (dom.hostAuthForm) {
        dom.hostAuthForm.addEventListener("submit", (event) => {
            event.preventDefault();
            const formData = new FormData(dom.hostAuthForm);
            const password = formData.get("hostPassword") || "";
            socket.emit("host:authorize", { password }, (res) => {
                if (res?.ok) {
                    togglePanels(true);
                    setAuthStatus("");
                    setHostStatus(ui("startConfigHint"), "info");
                } else {
                    togglePanels(false);
                    setAuthStatus(ui("authWrong"), "error");
                }
            });
        });
    }

    socket.on("session:players", ({ players }) => {
        dom.playerList.innerHTML = players.map(p => `<li>${p.nickname} (${p.score} pts)</li>`).join("");
    });

    socket.on("session:gameReady", ({ gameTitle, llmError }) => {
        dom.gameTitlePill.textContent = `${gameTitle.es} / ${gameTitle.en}`;
        dom.llmWarning.hidden = !llmError;
        if (!llmError) {
            setHostStatus(ui("gameReady"), "success");
        } else {
            setHostStatus(ui("llmFallbackShort"), "warning");
        }
    });

    socket.on("session:ready", () => {
        setHostStatus(ui("playersReady"));
    });

    socket.on("question:start", onQuestionStart);
    socket.on("question:results", onQuestionResults);
    socket.on("session:ranking", onRankingUpdate);
    socket.on("session:final", onFinalAwards);

    socket.on("session:ended", () => {
        setHostStatus(ui("sessionEnded"), "warning");
        stopCountdown();
    });

    socket.on("session:status", ({ message }) => {
        setHostStatus(message, "info");
    });

    applyPasswordHint();
    applyLanguagePreference();
    populatePredefined();
})();
