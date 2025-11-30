import { LLM_CONFIG, GAME_CONFIG } from "./config.js";
import { FALLBACK_GAME } from "./questions_fallback.js";

const state = {
    currentGame: null,
    currentQuestionIndex: 0,
    currentLanguage: GAME_CONFIG.defaultLanguage,
    currentEarnings: 0,
    selectedOption: null,
    lifelinesUsed: {
        hint: false,
        friend: false,
        fifty: false
    },
    loading: false,
    ladderPosition: "right",
    mode: "fallback",
    earnedLevels: new Set(),
    gameOver: false,
    lastMessage: null
};

const elements = {};

const formatCurrency = (amount, lang = state.currentLanguage) => {
    const locale = lang === "EN" ? "en-US" : "es-ES";
    return `$${amount.toLocaleString(locale)}`;
};

const setIdleLevelInfo = () => {
    if (!elements.levelInfo) return;
    const prizeEs = formatCurrency(0, "ES");
    const prizeEn = formatCurrency(0, "EN");
    elements.levelInfo.textContent = getSingleLine(
        `Nivel 0 · Premio ${prizeEs}`,
        `Level 0 · Prize ${prizeEn}`
    );
};

const init = () => {
    cacheElements();
    attachListeners();
    updateLadderPosition(state.ladderPosition);
    updateModeDisplay();
    renderMoneyLadder();
    updateLanguageButtons();
    updateHeaderTexts();
    setIdleLevelInfo();
    showLocalizedMessage("Selecciona cómo quieres iniciar la partida.", "Choose how you want to start the game.");
};

const cacheElements = () => {
    elements.title = document.getElementById("game-title");
    elements.tagline = document.getElementById("game-tagline");
    elements.languageButtons = document.querySelectorAll("[data-lang]");
    elements.startAI = document.getElementById("start-ai");
    elements.startFallback = document.getElementById("start-fallback");
    elements.levelInfo = document.getElementById("level-info");
    elements.context = document.getElementById("context");
    elements.question = document.getElementById("question");
    elements.options = document.getElementById("options");
    elements.confirm = document.getElementById("confirm-answer");
    elements.next = document.getElementById("next-question");
    elements.hint = document.getElementById("hint");
    elements.friend = document.getElementById("friend");
    elements.fifty = document.getElementById("fifty");
    elements.lifelineOutput = document.getElementById("lifeline-output");
    elements.messagePanel = document.getElementById("message-panel");
    elements.messageContent = document.getElementById("message-content");
    elements.restart = document.getElementById("restart-game");
    elements.moneyLadder = document.getElementById("money-ladder");
    elements.ladderLabelLevel = document.getElementById("ladder-label-level");
    elements.ladderLabelPrize = document.getElementById("ladder-label-prize");
    elements.modePill = document.getElementById("mode-pill");
    elements.modeIcon = elements.modePill ? elements.modePill.querySelector(".mode-icon") : null;
    elements.modeText = elements.modePill ? elements.modePill.querySelector(".mode-text") : null;
    elements.loadingOverlay = document.getElementById("loading-overlay");
    elements.loadingText = document.getElementById("loading-text");
    elements.ladderRightBtn = document.getElementById("ladder-right");
    elements.ladderBottomBtn = document.getElementById("ladder-bottom");
};

const attachListeners = () => {
    elements.languageButtons.forEach(btn => {
        btn.addEventListener("click", () => {
            state.currentLanguage = btn.dataset.lang;
            updateLanguageButtons();
            updateHeaderTexts();
            updateModeDisplay();
            renderQuestion();
            refreshLocalizedMessage();
            renderMoneyLadder();
        });
    });

    if (elements.ladderRightBtn) {
        elements.ladderRightBtn.addEventListener("click", () => updateLadderPosition("right"));
    }
    if (elements.ladderBottomBtn) {
        elements.ladderBottomBtn.addEventListener("click", () => updateLadderPosition("bottom"));
    }

    elements.startAI.addEventListener("click", () => startGame(true));
    elements.startFallback.addEventListener("click", () => startGame(false));
    elements.confirm.addEventListener("click", confirmAnswer);
    elements.next.addEventListener("click", nextQuestion);
    elements.hint.addEventListener("click", useHint);
    elements.friend.addEventListener("click", callFriend);
    elements.fifty.addEventListener("click", useFifty);

    if (elements.restart) {
        elements.restart.addEventListener("click", resetToWelcome);
    }
};

const renderMoneyLadder = () => {
    elements.moneyLadder.innerHTML = "";
    [...GAME_CONFIG.moneyLadder].reverse().forEach((amount, idx) => {
        const level = GAME_CONFIG.moneyLadder.length - idx;
        const li = document.createElement("li");
        li.dataset.level = level;
        const formatted = formatCurrency(amount);
        li.innerHTML = `
            <span class="ladder-level">${level}</span>
            <div class="ladder-prize">
                <strong>${formatted}</strong>
                <span class="prize-icon" aria-hidden="true">🏆</span>
            </div>
        `;
        elements.moneyLadder.appendChild(li);
    });
    highlightLadder();
};

const highlightLadder = () => {
    const hasGame = Boolean(state.currentGame);
    const level = state.currentQuestionIndex + 1;
    elements.moneyLadder.querySelectorAll("li").forEach(li => {
        const liLevel = Number(li.dataset.level);
        li.classList.toggle("active", hasGame && liLevel === level);
        li.classList.toggle("earned", state.earnedLevels.has(liLevel));
    });
};

const updateLanguageButtons = () => {
    elements.languageButtons.forEach(btn => {
        btn.classList.toggle("active", btn.dataset.lang === state.currentLanguage);
    });
};

const startGame = async (useAI) => {
    if (state.loading) return;
    state.loading = true;
    toggleStartButtons(true);
    resetState();
    const startEs = useAI ? "Generando juego con IA..." : "Cargando preguntas de reserva...";
    const startEn = useAI ? "Generating quiz with AI..." : "Loading fallback questions...";
    showLocalizedMessage(startEs, startEn);

    let mode = "fallback";

    if (useAI) {
        setLoadingOverlay(true, getSingleLine("Generando juego con IA...", "Generating quiz with AI..."));
        try {
            const generated = await generateGameFromLLM();
            if (generated) {
                state.currentGame = generated;
                showLocalizedMessage("Juego preparado con IA.", "LLM quiz ready.");
                mode = "ai";
            } else {
                state.currentGame = FALLBACK_GAME;
                showLocalizedMessage(
                    "No se ha podido generar el juego con el modelo de IA. Se usará la batería de preguntas de reserva.",
                    "The quiz could not be generated with the LLM. The fallback question set will be used."
                );
            }
        } finally {
            setLoadingOverlay(false);
        }
    } else {
        state.currentGame = FALLBACK_GAME;
        showLocalizedMessage("Usando preguntas de reserva.", "Using fallback questions.");
    }

    setMode(mode);
    renderGameMeta();
    renderQuestion();
    toggleStartButtons(false);
    state.loading = false;
};

const toggleStartButtons = (disabled) => {
    [elements.startAI, elements.startFallback].forEach(btn => {
        btn.disabled = disabled;
        btn.classList.toggle("loading", disabled);
    });
};

const resetState = () => {
    state.currentGame = null;
    state.currentQuestionIndex = 0;
    state.currentEarnings = 0;
    state.selectedOption = null;
    state.lifelinesUsed = { hint: false, friend: false, fifty: false };
    state.earnedLevels = new Set();
    state.gameOver = false;
    elements.confirm.disabled = true;
    elements.next.classList.add("hidden");
    if (elements.lifelineOutput) {
        elements.lifelineOutput.innerHTML = "";
    }
    [elements.hint, elements.friend, elements.fifty].forEach(btn => {
        btn.disabled = false;
        btn.classList.remove("used");
    });
    if (elements.context) elements.context.innerHTML = "";
    if (elements.question) elements.question.innerHTML = "";
    if (elements.options) elements.options.innerHTML = "";
    setIdleLevelInfo();
    toggleRestartButton(false);
    highlightLadder();
};

const renderGameMeta = () => {
    updateHeaderTexts();
};

const renderQuestion = () => {
    if (!state.currentGame) {
        setIdleLevelInfo();
        return;
    }
    const question = state.currentGame.questions[state.currentQuestionIndex];
    if (!question) {
        handleWin();
        return;
    }

    highlightLadder();
    const prizeEs = formatCurrency(question.amount, "ES");
    const prizeEn = formatCurrency(question.amount, "EN");
    elements.levelInfo.textContent = getText(
        `Nivel ${question.level} · Premio ${prizeEs}`,
        `Level ${question.level} · Prize ${prizeEn}`
    );
    elements.context.innerHTML = wrapParagraph(getText(question.context_es, question.context_en));
    elements.question.innerHTML = wrapParagraph(getText(question.question_es, question.question_en));

    state.selectedOption = null;
    elements.confirm.disabled = true;
    elements.next.classList.add("hidden");
    if (elements.lifelineOutput) {
        elements.lifelineOutput.innerHTML = "";
    }
    renderOptions(question);
};

function getText(es, en) {
    return state.currentLanguage === "EN" ? en : es;
}

function wrapParagraph(text) {
    return `<p>${text}</p>`;
}

function getSingleLine(es, en) {
    return getText(es, en);
}

const updateHeaderTexts = () => {
    elements.title.textContent = getText("Quien quiere ser ISOmillonario", "Who wants to be ISOmillionaire");
    if (elements.tagline) {
        elements.tagline.textContent = getText("Retos sobre ISO 9241 · 29148 · 25010", "Challenges around ISO 9241 · 29148 · 25010");
    }
    if (elements.ladderLabelLevel) {
        elements.ladderLabelLevel.textContent = getSingleLine("Nivel", "Level");
    }
    if (elements.ladderLabelPrize) {
        elements.ladderLabelPrize.textContent = getSingleLine("Premio", "Prize");
    }
    if (elements.restart) {
        elements.restart.textContent = getSingleLine("Empezar de nuevo", "Play again");
    }
    updateButtonTexts();
};

const updateButtonTexts = () => {
    if (elements.startAI) {
        elements.startAI.textContent = getSingleLine("Empezar con IA", "Start with AI");
    }
    if (elements.startFallback) {
        elements.startFallback.textContent = getSingleLine("Preguntas de reserva", "Fallback questions");
    }
    if (elements.confirm) {
        elements.confirm.textContent = getSingleLine("Responder", "Answer");
    }
    if (elements.next) {
        elements.next.textContent = getSingleLine("Siguiente pregunta", "Next question");
    }
    if (elements.hint) {
        const label = elements.hint.querySelector(".btn-label");
        if (label) label.textContent = getSingleLine("Pista", "Hint");
    }
    if (elements.friend) {
        const label = elements.friend.querySelector(".btn-label");
        if (label) label.textContent = getSingleLine("Llamada", "Phone a friend");
    }
    if (elements.fifty) {
        const label = elements.fifty.querySelector(".btn-label");
        if (label) label.textContent = getSingleLine("50/50", "50/50");
    }
    if (elements.ladderRightBtn) {
        elements.ladderRightBtn.setAttribute("aria-label", getSingleLine("Mostrar ranking a la derecha", "Show ladder on the right"));
    }
    if (elements.ladderBottomBtn) {
        elements.ladderBottomBtn.setAttribute("aria-label", getSingleLine("Mostrar ranking debajo", "Show ladder below"));
    }
};

const renderOptions = (question) => {
    elements.options.innerHTML = "";
    const labels = state.currentLanguage === "EN" ? question.options_en : question.options_es;
    labels.forEach((label, idx) => {
        const btn = document.createElement("button");
        btn.className = "option-btn";
        btn.dataset.index = idx;
        btn.innerHTML = `<span class="option-label">${label}</span><span class="win-icon" aria-hidden="true">🏆</span>`;
        btn.addEventListener("click", () => selectOption(idx));
        elements.options.appendChild(btn);
    });
};

const selectOption = (idx) => {
    if (!state.currentGame) return;
    const buttons = elements.options.querySelectorAll(".option-btn");
    buttons.forEach(btn => btn.classList.remove("selected"));
    const chosen = buttons[idx];
    if (chosen.disabled) return;
    state.selectedOption = idx;
    chosen.classList.add("selected");
    elements.confirm.disabled = false;
    showLocalizedMessage("Confirma tu respuesta cuando estés listo.", "Confirm your answer when ready.");
};

const confirmAnswer = () => {
    if (state.selectedOption === null || !state.currentGame) return;
    const question = state.currentGame.questions[state.currentQuestionIndex];
    const buttons = elements.options.querySelectorAll(".option-btn");
    buttons.forEach(btn => btn.disabled = true);
    const isCorrect = state.selectedOption === question.correct_index;
    const selectedBtn = buttons[state.selectedOption];
    selectedBtn.classList.add(isCorrect ? "correct" : "incorrect");
    buttons[question.correct_index].classList.add("correct", "winner");
    selectedBtn.classList.toggle("winner", isCorrect);

    if (isCorrect) {
        state.currentEarnings = question.amount;
        state.earnedLevels.add(question.level);
        highlightLadder();
        elements.next.classList.remove("hidden");
        showLocalizedMessage("¡Correcto! Pulsa siguiente pregunta.", "Correct! Move to the next question.");
        launchConfetti();
    } else {
        handleLoss();
    }

    elements.confirm.disabled = true;
};

const nextQuestion = () => {
    state.currentQuestionIndex += 1;
    state.selectedOption = null;
    elements.next.classList.add("hidden");
    renderQuestion();
};

const handleLoss = () => {
    const prizeEs = formatCurrency(state.currentEarnings, "ES");
    const prizeEn = formatCurrency(state.currentEarnings, "EN");
    showGameOverState(
        `Juego terminado. Premio final: ${prizeEs}.`,
        `Game over. Final prize: ${prizeEn}.`
    );
};

const handleWin = () => {
    showGameOverState(
        "¡Felicidades! ¡Eres ISOmillonario!",
        "Congratulations! You are the ISOmillionaire!"
    );
    launchConfetti(true);
};

const useHint = () => {
    if (!state.currentGame || state.lifelinesUsed.hint) return;
    state.lifelinesUsed.hint = true;
    elements.hint.disabled = true;
    elements.hint.classList.add("used");
    const question = state.currentGame.questions[state.currentQuestionIndex];
    elements.lifelineOutput.innerHTML = `<strong>${getSingleLine("Pista", "Hint")}:</strong> ${getText(question.hint_es, question.hint_en)}`;
};

const callFriend = () => {
    if (!state.currentGame || state.lifelinesUsed.friend) return;
    state.lifelinesUsed.friend = true;
    elements.friend.disabled = true;
    elements.friend.classList.add("used");
    const question = state.currentGame.questions[state.currentQuestionIndex];
    const friendCopy = `${getText(question.friend_answer_es, question.friend_answer_en)}<p>${getSingleLine(`Confianza: ${question.friend_confidence}`, `Confidence: ${question.friend_confidence}`)}</p>`;
    elements.lifelineOutput.innerHTML = `<strong>${getSingleLine("Amigo", "Friend")}:</strong> ${friendCopy}`;
    speakText(question.friend_answer_en);
};

const speakText = (text) => {
    if (!("speechSynthesis" in window)) return;
    const utterance = new SpeechSynthesisUtterance(text);
    window.speechSynthesis.speak(utterance);
};

const useFifty = () => {
    if (!state.currentGame || state.lifelinesUsed.fifty) return;
    const question = state.currentGame.questions[state.currentQuestionIndex];
    state.lifelinesUsed.fifty = true;
    elements.fifty.disabled = true;
    elements.fifty.classList.add("used");
    const incorrect = [0, 1, 2, 3].filter(idx => idx !== question.correct_index);
    incorrect.sort((a, b) => difficultyRank(question.option_difficulty[a]) - difficultyRank(question.option_difficulty[b]));
    const toDisable = incorrect.slice(0, 2);
    const buttons = elements.options.querySelectorAll(".option-btn");
    toDisable.forEach(idx => {
        const btn = buttons[idx];
        btn.disabled = true;
        btn.classList.add("disabled");
    });
    elements.lifelineOutput.innerHTML = getSingleLine("Se han eliminado dos opciones.", "Two options have been removed.");
};

const difficultyRank = (difficulty) => {
    return { easy: 1, medium: 2, hard: 3 }[difficulty] || 4;
};

const generateGameFromLLM = async () => {
    if (!LLM_CONFIG.enabled) return null;
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), LLM_CONFIG.timeoutMs);
    const prompt = buildLLMPrompt();

    try {
        const response = await fetch(LLM_CONFIG.baseUrl, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ model: LLM_CONFIG.model, prompt, stream: false }),
            signal: controller.signal
        });
        clearTimeout(timeoutId);

        if (!response.ok) throw new Error(`HTTP ${response.status}`);
        const payload = await response.text();
        const parsed = parseLLMPayload(payload);
        validateGame(parsed);
        return parsed;
    } catch (error) {
        clearTimeout(timeoutId);
        console.error("LLM generation failed", error);
        return null;
    }
};

const buildLLMPrompt = () => {
    return `You are generating a Spanish/English bilingual quiz called Quien quiere ser ISOmillonario. Return ONLY a valid JSON object with this exact structure:
{
  "game_title_es": "Quien quiere ser ISOmillonario",
  "game_title_en": "Who wants to be ISOmillionaire",
  "iso_focus": ["ISO 9241", "ISO/IEC/IEEE 29148", "ISO/IEC 25010:2023"],
  "questions": [
    {
      "id": "q1",
      "level": 1,
      "amount": 100,
      "iso_standard": "ISO 9241",
      "context_es": "...",
      "context_en": "...",
      "question_es": "...",
      "question_en": "...",
      "options_es": ["A","B","C","D"],
      "options_en": ["A","B","C","D"],
      "correct_index": 0,
      "option_difficulty": ["easy","medium","hard","easy"],
      "hint_es": "...",
      "hint_en": "...",
      "friend_answer_es": "...",
      "friend_answer_en": "...",
      "friend_confidence": "high"
    }
  ]
}
Provide exactly ${GAME_CONFIG.totalQuestions} questions (levels 1-15). Contexts must describe realistic software or interactive systems. Distribute ISO standards across the set. Use only the values "easy", "medium", "hard" for option_difficulty entries and "high", "medium", "low" for friend_confidence. No extra commentary before or after the JSON.`;
};

const parseLLMPayload = (data) => {
    try {
        const json = JSON.parse(data);
        if (json && typeof json === "object" && json.questions) return json;
        if (json && json.response) {
            const extracted = extractJSONObject(json.response);
            if (extracted) return extracted;
        }
    } catch (err) {
        const extracted = extractJSONObject(data);
        if (extracted) return extracted;
    }
    throw new Error("Unable to parse LLM payload");
};

const extractJSONObject = (text) => {
    const match = text.match(/\{[\s\S]*\}/);
    return match ? JSON.parse(match[0]) : null;
};

const validateGame = (game) => {
    if (!game || !Array.isArray(game.questions) || game.questions.length !== GAME_CONFIG.totalQuestions) {
        throw new Error("Game payload invalid");
    }
};

const showMessage = (content) => {
    if (elements.messageContent) {
        elements.messageContent.innerHTML = content;
    } else if (elements.messagePanel) {
        elements.messagePanel.innerHTML = content;
    }
};

const showLocalizedMessage = (messageEs, messageEn) => {
    state.lastMessage = { es: messageEs, en: messageEn };
    showMessage(getSingleLine(messageEs, messageEn));
};

const refreshLocalizedMessage = () => {
    if (!state.lastMessage) return;
    const { es, en } = state.lastMessage;
    showMessage(getSingleLine(es, en));
};

const toggleRestartButton = (visible) => {
    if (!elements.restart) return;
    if (visible) {
        elements.restart.textContent = getSingleLine("Empezar de nuevo", "Play again");
    }
    elements.restart.classList.toggle("hidden", !visible);
    elements.restart.disabled = !visible;
};

function resetToWelcome() {
    state.currentGame = null;
    resetState();
    showLocalizedMessage(
        "Selecciona cómo quieres iniciar la partida.",
        "Choose how you want to start the game."
    );
}

const showGameOverState = (messageEs, messageEn) => {
    state.gameOver = true;
    showLocalizedMessage(messageEs, messageEn);
    toggleRestartButton(true);
};

const updateLadderPosition = (position) => {
    state.ladderPosition = position;
    document.body.classList.remove("ladder-right", "ladder-bottom");
    document.body.classList.add(`ladder-${position}`);
    updateLadderToggle();
};

const updateLadderToggle = () => {
    const isRight = state.ladderPosition === "right";
    if (elements.ladderRightBtn) {
        elements.ladderRightBtn.setAttribute("aria-pressed", isRight ? "true" : "false");
        elements.ladderRightBtn.title = getSingleLine("Ranking a la derecha", "Ranking on the right");
    }
    if (elements.ladderBottomBtn) {
        elements.ladderBottomBtn.setAttribute("aria-pressed", !isRight ? "true" : "false");
        elements.ladderBottomBtn.title = getSingleLine("Ranking debajo", "Ranking below");
    }
};

const setMode = (mode) => {
    state.mode = mode;
    updateModeDisplay();
};

const updateModeDisplay = () => {
    document.body.classList.remove("mode-ai", "mode-fallback");
    document.body.classList.add(`mode-${state.mode}`);
    if (elements.modeIcon) {
        elements.modeIcon.textContent = state.mode === "ai" ? "🤖" : "🛡️";
    }
    if (elements.modeText) {
        elements.modeText.textContent = state.mode === "ai"
            ? getSingleLine("Modo IA activo", "AI mode active")
            : getSingleLine("Modo reserva", "Offline mode");
    }
};

const launchConfetti = (isFinal = false) => {
    const container = document.createElement("div");
    container.className = "confetti-container";
    const pieces = isFinal ? 80 : 40;
    for (let i = 0; i < pieces; i += 1) {
        const piece = document.createElement("span");
        piece.className = "confetti-piece";
        piece.style.left = `${Math.random() * 100}%`;
        piece.style.backgroundColor = `hsl(${Math.random() * 360}, 80%, 60%)`;
        piece.style.animationDelay = `${Math.random() * 0.3}s`;
        piece.style.width = `${8 + Math.random() * 6}px`;
        container.appendChild(piece);
    }
    document.body.appendChild(container);
    setTimeout(() => container.remove(), 1700);
};

const setLoadingOverlay = (visible, message) => {
    if (!elements.loadingOverlay) return;
    if (message && elements.loadingText) {
        elements.loadingText.textContent = message;
    }
    elements.loadingOverlay.classList.toggle("hidden", !visible);
};

document.addEventListener("DOMContentLoaded", init);
