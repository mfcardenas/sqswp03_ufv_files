(() => {
    const socket = io();

    const dom = {
        playerForm: document.getElementById("player-form"),
        playerStatus: document.getElementById("player-status"),
        playerQuestionCard: document.getElementById("player-question-card"),
        playerTimer: document.getElementById("player-timer"),
        playerQuestion: document.getElementById("player-question"),
        playerOptions: document.getElementById("player-options"),
        playerFeedback: document.getElementById("player-feedback"),
        playerRanking: document.getElementById("player-ranking"),
        rankingTemplate: document.getElementById("ranking-template")
    };

    const uiLang = document.body?.dataset?.uiLang === "en" ? "en" : "es";
    const UI_TEXT = {
        es: {
            sessionNotFound: "El código no existe.",
            waitingHost: "Esperando al docente",
            gameStartingSoon: "La partida inicia pronto",
            sessionEnded: "Sesión finalizada",
            connecting: "Conectando...",
            rankingTitle: "Ranking"
        },
        en: {
            sessionNotFound: "Session code not found.",
            waitingHost: "Waiting for the host",
            gameStartingSoon: "The match will start soon",
            sessionEnded: "Session ended",
            connecting: "Connecting...",
            rankingTitle: "Leaderboard"
        }
    };

    const ui = (key) => UI_TEXT[uiLang]?.[key] || key;

    const state = {
        sessionCode: null,
        nickname: null,
        language: "ES",
        countdownId: null,
        hasAnswered: false,
        currentQuestion: null
    };

    const text = (es, en) => {
        if (state.language === "EN") return en;
        if (state.language === "BI") return `${es}\n${en}`;
        return es;
    };

    const setPlayerStatus = (message, type = "info") => {
        dom.playerStatus.innerHTML = `<span class="${type}">${message}</span>`;
    };

    const renderRanking = (ranking) => {
        if (!ranking || ranking.length === 0) {
            dom.playerRanking.innerHTML = "";
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
        dom.playerRanking.innerHTML = "";
        dom.playerRanking.appendChild(clone);
    };

    const stopCountdown = () => {
        if (state.countdownId) {
            clearInterval(state.countdownId);
            state.countdownId = null;
        }
    };

    const resetPlayerView = () => {
        stopCountdown();
        state.currentQuestion = null;
        state.hasAnswered = false;
        dom.playerQuestionCard.hidden = true;
        dom.playerQuestion.innerHTML = "";
        dom.playerOptions.innerHTML = "";
        dom.playerFeedback.textContent = "";
        dom.playerFeedback.className = "feedback";
        dom.playerRanking.innerHTML = "";
    };

    const startCountdown = (seconds) => {
        stopCountdown();
        let remaining = seconds;
        dom.playerTimer.textContent = remaining.toString().padStart(2, "0");
        state.countdownId = setInterval(() => {
            remaining -= 1;
            dom.playerTimer.textContent = remaining.toString().padStart(2, "0");
            if (remaining <= 0) {
                stopCountdown();
            }
        }, 1000);
    };

    const formatQuestionHTML = (payload) => {
        const ctx = state.language === "EN" ? payload.context.en : payload.context.es;
        const ctxBi = state.language === "BI" ? `<p>${payload.context.es}</p><p class="muted">${payload.context.en}</p>` : `<p>${ctx}</p>`;
        const q = state.language === "EN" ? payload.question.en : payload.question.es;
        const qBi = state.language === "BI" ? `<h3>${payload.question.es}</h3><p class="muted">${payload.question.en}</p>` : `<h3>${q}</h3>`;
        return `${ctxBi}${qBi}<p class="tag">${payload.iso_standard} · ${payload.difficulty}</p>`;
    };

    const renderOptions = (payload) => {
        const options = state.language === "EN" ? payload.options.en : payload.options.es;
        const optionsBi = payload.options;
        dom.playerOptions.innerHTML = "";
        options.forEach((label, idx) => {
            const btn = document.createElement("button");
            btn.type = "button";
            btn.dataset.index = idx;
            if (state.language === "BI") {
                btn.innerHTML = `<strong>${optionsBi.es[idx]}</strong><br><span class="muted">${optionsBi.en[idx]}</span>`;
            } else {
                btn.textContent = label;
            }
            btn.addEventListener("click", () => handlePlayerAnswer(idx));
            dom.playerOptions.appendChild(btn);
        });
    };

    const handlePlayerAnswer = (choice) => {
        if (state.hasAnswered || !state.currentQuestion) return;
        state.hasAnswered = true;
        dom.playerOptions.querySelectorAll("button").forEach(btn => btn.disabled = true);
        socket.emit("player:submitAnswer", {
            code: state.sessionCode,
            questionId: state.currentQuestion.id,
            choice
        });
    };

    const onQuestionStart = ({ question, timerSeconds, language }) => {
        state.language = language || state.language || "ES";
        state.currentQuestion = question;
        state.hasAnswered = false;
        dom.playerQuestionCard.hidden = false;
        dom.playerFeedback.textContent = "";
        dom.playerFeedback.className = "feedback";
        dom.playerQuestion.innerHTML = formatQuestionHTML(question);
        renderOptions(question);
        dom.playerOptions.querySelectorAll("button").forEach(btn => btn.disabled = false);
        startCountdown(timerSeconds);
    };

    const onPlayerFeedback = (payload) => {
        const message = payload.correct
            ? text("✅ ¡Respuesta correcta!", "✅ Correct answer!")
            : text("❌ Respuesta incorrecta", "❌ Incorrect answer");
        dom.playerFeedback.textContent = `${message} · ${payload.points} pts`;
        dom.playerFeedback.className = `feedback ${payload.correct ? "correct" : "incorrect"}`;
        stopCountdown();
    };

    const onRankingUpdate = ({ ranking }) => {
        renderRanking(ranking);
    };

    const onFinalAwards = ({ ranking, awards }) => {
        const top = awards.topScorer ? `${awards.topScorer.nickname} · ${awards.topScorer.score} pts` : text("Sin datos", "No data");
        const fast = awards.fastest ? `${awards.fastest.nickname} (${awards.fastest.fastestMs?.toFixed(1)}s)` : text("Sin ganador veloz", "No fastest player");
        dom.playerFeedback.innerHTML = `
            <h3>${text("Ranking final","Final ranking")}</h3>
            <p>${text("Máxima puntuación","Top scorer")}: ${top}</p>
            <p>${text("Más rápido (>=50% aciertos)", "Fastest (>=50% correct)")}: ${fast}</p>
        `;
        renderRanking(ranking);
        stopCountdown();
    };

    dom.playerForm.addEventListener("submit", (event) => {
        event.preventDefault();
        const formData = new FormData(dom.playerForm);
        const nickname = formData.get("nickname");
        const code = (formData.get("sessionCode") || "").trim().toUpperCase();
        resetPlayerView();
        setPlayerStatus(ui("connecting"));
        socket.emit("player:joinSession", { nickname, code }, (res) => {
            if (!res?.ok) {
                setPlayerStatus(ui("sessionNotFound"), "error");
                return;
            }
            state.sessionCode = code;
            state.nickname = nickname;
            state.language = res.language;
            setPlayerStatus(ui("waitingHost"), "success");
            dom.playerQuestionCard.hidden = false;
        });
    });

    socket.on("question:start", onQuestionStart);
    socket.on("question:feedback", onPlayerFeedback);
    socket.on("session:ranking", onRankingUpdate);
    socket.on("session:final", onFinalAwards);

    socket.on("session:ready", () => {
        setPlayerStatus(ui("gameStartingSoon"));
    });

    socket.on("session:ended", () => {
        setPlayerStatus(ui("sessionEnded"), "warning");
        state.sessionCode = null;
        resetPlayerView();
    });
})();
