/**
 * persistence.js
 * ─────────────────────────────────────────────────────────
 * Observa el juego ISOmillonario **sin modificarlo** y
 * persiste cada sesión de juego vía API REST.
 *
 * Se añade al HTML con: <script type="module" src="./persistence.js"></script>
 * ─────────────────────────────────────────────────────────
 */

const API_BASE = "/api";

/* ───── Traducciones ───── */
const i18n = {
    EN: {
        modalTitle: "🎮 Player Registration",
        modalDesc: "Enter your name and university to save your progress.",
        labelNickname: "Nickname",
        labelUniversity: "University",
        placeholderNick: "Your nickname",
        placeholderUni: "Your university",
        btnSubmit: "Register & Play",
        btnSubmitting: "Registering...",
        errRequired: "Both fields are required.",
        errRegister: "Registration error.",
        errConnection: "Connection error with the server.",
        logoutTitle: "Log out",
    },
    ES: {
        modalTitle: "🎮 Registro de jugador",
        modalDesc: "Introduce tu nombre y universidad para guardar tu progreso.",
        labelNickname: "Nickname",
        labelUniversity: "Universidad",
        placeholderNick: "Tu nickname",
        placeholderUni: "Tu universidad",
        btnSubmit: "Registrarse y jugar",
        btnSubmitting: "Registrando...",
        errRequired: "Ambos campos son obligatorios.",
        errRegister: "Error al registrar.",
        errConnection: "Error de conexión con el servidor.",
        logoutTitle: "Cerrar sesión",
    },
};

function getCurrentLang() {
    const active = document.querySelector(".lang-btn.active");
    return active ? active.dataset.lang : "EN";
}

function t(key) {
    return (i18n[getCurrentLang()] || i18n.EN)[key] || key;
}

/* ───── Estado de persistencia ───── */
const pState = {
    userId: null,
    nickname: null,
    university: null,
    sessionId: null,
    startedAt: null,
    mode: "fallback",
    language: "EN",
    questionsLog: [],
    currentLevel: 0,
    correctCount: 0,
    incorrectCount: 0,
    currentScore: 0,
    lifelinesUsed: { hint: false, friend: false, fifty: false },
    levelsEarned: [],
    registered: false,
    sessionActive: false,
};

/* ═══════════════════════════════════════════════════════
   1. FORMULARIO DE REGISTRO (modal antes de jugar)
   ═══════════════════════════════════════════════════════ */

function injectRegistrationModal() {
    // Recuperar datos previos de localStorage
    const saved = localStorage.getItem("iso_player");
    if (saved) {
        try {
            const data = JSON.parse(saved);
            pState.nickname = data.nickname;
            pState.university = data.university;
            pState.userId = data.userId;
            pState.registered = true;
            showPlayerBadge();
            return; // Ya registrado en este navegador
        } catch { /* ignorar */ }
    }

    // Deshabilitar botones de inicio hasta que se registre
    const startAI = document.getElementById("start-ai");
    const startFallback = document.getElementById("start-fallback");
    if (startAI) startAI.disabled = true;
    if (startFallback) startFallback.disabled = true;

    // Crear modal
    const overlay = document.createElement("div");
    overlay.id = "persist-modal-overlay";
    overlay.style.cssText = `
    position:fixed; inset:0; z-index:9999;
    background:rgba(0,0,0,0.7); backdrop-filter:blur(6px);
    display:flex; align-items:center; justify-content:center;
    font-family:inherit;
  `;

    overlay.innerHTML = `
    <div style="
      background:linear-gradient(145deg,#1a1a2e,#16213e);
      border:1px solid rgba(255,215,0,0.3); border-radius:16px;
      padding:32px; max-width:380px; width:90%;
      box-shadow:0 20px 60px rgba(0,0,0,0.6); color:#f0e6d3;
    ">
      <h2 id="persist-title" style="margin:0 0 8px; color:#ffd700; font-size:1.4rem; text-align:center;"></h2>
      <p id="persist-desc" style="margin:0 0 20px; text-align:center; font-size:0.9rem; opacity:0.8;"></p>
      <label id="persist-label-nick" style="display:block; margin-bottom:4px; font-size:0.85rem; color:#ccc;"></label>
      <input id="persist-nickname" type="text" maxlength="30" required
        style="
          width:100%; padding:10px 12px; margin-bottom:14px;
          border:1px solid rgba(255,215,0,0.3); border-radius:8px;
          background:rgba(255,255,255,0.08); color:#fff; font-size:1rem;
          box-sizing:border-box; outline:none;
        " />
      <label id="persist-label-uni" style="display:block; margin-bottom:4px; font-size:0.85rem; color:#ccc;"></label>
      <input id="persist-university" type="text" maxlength="60" required
        style="
          width:100%; padding:10px 12px; margin-bottom:20px;
          border:1px solid rgba(255,215,0,0.3); border-radius:8px;
          background:rgba(255,255,255,0.08); color:#fff; font-size:1rem;
          box-sizing:border-box; outline:none;
        " />
      <div id="persist-error" style="
        color:#ff6b6b; font-size:0.85rem; margin-bottom:10px;
        min-height:1.2em; text-align:center;
      "></div>
      <button id="persist-submit" style="
        width:100%; padding:12px; border:none; border-radius:8px;
        background:linear-gradient(135deg,#ffd700,#ffaa00);
        color:#1a1a2e; font-weight:700; font-size:1rem;
        cursor:pointer; transition:opacity 0.2s;
      "></button>
    </div>
  `;

    document.body.appendChild(overlay);
    updateModalLang(); // Apply current language to the modal

    // Handler
    document.getElementById("persist-submit").addEventListener("click", async () => {
        const nick = document.getElementById("persist-nickname").value.trim();
        const uni = document.getElementById("persist-university").value.trim();
        const errEl = document.getElementById("persist-error");

        if (!nick || !uni) {
            errEl.textContent = t("errRequired");
            return;
        }

        errEl.textContent = "";
        document.getElementById("persist-submit").disabled = true;
        document.getElementById("persist-submit").textContent = t("btnSubmitting");

        try {
            const res = await fetch(`${API_BASE}/players`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ nickname: nick, university: uni }),
            });

            const data = await res.json();

            if (!res.ok) {
                errEl.textContent = data.error || t("errRegister");
                document.getElementById("persist-submit").disabled = false;
                document.getElementById("persist-submit").textContent = t("btnSubmit");
                return;
            }

            pState.userId = data.user_id;
            pState.nickname = nick;
            pState.university = uni;
            pState.registered = true;

            localStorage.setItem(
                "iso_player",
                JSON.stringify({ userId: data.user_id, nickname: nick, university: uni })
            );

            overlay.remove();
            showPlayerBadge();
            if (startAI) startAI.disabled = false;
            if (startFallback) startFallback.disabled = false;
        } catch (err) {
            errEl.textContent = t("errConnection");
            document.getElementById("persist-submit").disabled = false;
            document.getElementById("persist-submit").textContent = t("btnSubmit");
            console.error("Registration error:", err);
        }
    });

    // Enter key submits
    overlay.addEventListener("keydown", (e) => {
        if (e.key === "Enter") document.getElementById("persist-submit").click();
    });
}

/* ═══════════════════════════════════════════════════════
   1b. ACTUALIZAR IDIOMA DEL MODAL EN VIVO
   ═══════════════════════════════════════════════════════ */

function updateModalLang() {
    const title = document.getElementById("persist-title");
    const desc = document.getElementById("persist-desc");
    const labelNick = document.getElementById("persist-label-nick");
    const labelUni = document.getElementById("persist-label-uni");
    const nickInput = document.getElementById("persist-nickname");
    const uniInput = document.getElementById("persist-university");
    const submitBtn = document.getElementById("persist-submit");
    if (!title) return; // modal not visible

    title.textContent = t("modalTitle");
    desc.textContent = t("modalDesc");
    labelNick.textContent = t("labelNickname");
    labelUni.textContent = t("labelUniversity");
    if (nickInput) nickInput.placeholder = t("placeholderNick");
    if (uniInput) uniInput.placeholder = t("placeholderUni");
    if (submitBtn && !submitBtn.disabled) submitBtn.textContent = t("btnSubmit");
}

function listenLanguageSwitch() {
    document.querySelectorAll(".lang-btn").forEach((btn) => {
        btn.addEventListener("click", () => {
            // Update modal if visible
            updateModalLang();
            // Update badge logout tooltip if visible
            const logoutBtn = document.querySelector("#persist-player-badge button");
            if (logoutBtn) logoutBtn.title = t("logoutTitle");
        });
    });
}

/* ═══════════════════════════════════════════════════════
   1c. BADGE DE JUGADOR + CERRAR SESIÓN
   ═══════════════════════════════════════════════════════ */

function showPlayerBadge() {
    // Remove existing badge if any
    const existing = document.getElementById("persist-player-badge");
    if (existing) existing.remove();

    const badge = document.createElement("div");
    badge.id = "persist-player-badge";
    badge.style.cssText = `
        display:flex; align-items:center; gap:10px;
        padding:6px 14px; border-radius:20px;
        background:linear-gradient(135deg,rgba(255,215,0,0.15),rgba(255,170,0,0.10));
        border:1px solid rgba(255,215,0,0.35);
        color:#ffd700; font-size:0.85rem; font-weight:600;
        backdrop-filter:blur(4px);
    `;

    const info = document.createElement("span");
    info.innerHTML = `🎮 <strong>${pState.nickname}</strong> · ${pState.university}`;
    info.style.cssText = "white-space:nowrap; overflow:hidden; text-overflow:ellipsis; max-width:200px;";

    const logoutBtn = document.createElement("button");
    logoutBtn.textContent = "✕";
    logoutBtn.title = t("logoutTitle");
    logoutBtn.style.cssText = `
        background:rgba(255,100,100,0.2); border:1px solid rgba(255,100,100,0.4);
        color:#ff6b6b; border-radius:50%; width:24px; height:24px;
        cursor:pointer; font-size:0.8rem; font-weight:700;
        display:flex; align-items:center; justify-content:center;
        transition:background 0.2s;
        padding:0; line-height:1;
    `;
    logoutBtn.addEventListener("mouseenter", () => {
        logoutBtn.style.background = "rgba(255,100,100,0.4)";
    });
    logoutBtn.addEventListener("mouseleave", () => {
        logoutBtn.style.background = "rgba(255,100,100,0.2)";
    });
    logoutBtn.addEventListener("click", handleLogout);

    badge.appendChild(info);
    badge.appendChild(logoutBtn);

    // Insert into the header-top div, next to lang-switch
    const headerTop = document.querySelector(".header-top");
    if (headerTop) {
        headerTop.style.display = "flex";
        headerTop.style.alignItems = "center";
        headerTop.style.gap = "12px";
        headerTop.appendChild(badge);
    } else {
        // Fallback: insert at top of body
        badge.style.position = "fixed";
        badge.style.top = "10px";
        badge.style.right = "10px";
        badge.style.zIndex = "9998";
        document.body.appendChild(badge);
    }
}

async function handleLogout() {
    // If a session is active, mark it as ABANDONED
    if (pState.sessionActive && pState.sessionId) {
        await finishSession("ABANDONED");
    }

    // Clear state
    pState.userId = null;
    pState.nickname = null;
    pState.university = null;
    pState.sessionId = null;
    pState.registered = false;
    pState.sessionActive = false;

    // Clear localStorage
    localStorage.removeItem("iso_player");

    // Remove badge
    const badge = document.getElementById("persist-player-badge");
    if (badge) badge.remove();

    // Re-show registration modal
    injectRegistrationModal();
}

/* ═══════════════════════════════════════════════════════
   2. INTERCEPTAR INICIO DE PARTIDA
   ═══════════════════════════════════════════════════════ */

function interceptGameStart() {
    const startAI = document.getElementById("start-ai");
    const startFallback = document.getElementById("start-fallback");

    const handler = (isAI) => async () => {
        if (!pState.registered) return;

        pState.mode = isAI ? "ai" : "fallback";
        pState.startedAt = Date.now();
        pState.questionsLog = [];
        pState.currentLevel = 0;
        pState.correctCount = 0;
        pState.incorrectCount = 0;
        pState.currentScore = 0;
        pState.lifelinesUsed = { hint: false, friend: false, fifty: false };
        pState.levelsEarned = [];
        pState.sessionActive = false;

        // Detect language from active button
        const activeLang = document.querySelector("[data-lang].active");
        pState.language = activeLang ? activeLang.dataset.lang : "ES";

        try {
            const res = await fetch(`${API_BASE}/sessions`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    user_id: pState.userId,
                    nickname: pState.nickname,
                    university: pState.university,
                    mode: pState.mode,
                }),
            });
            const data = await res.json();
            if (res.ok) {
                pState.sessionId = data.session_id;
                pState.sessionActive = true;
            }
        } catch (err) {
            console.error("Session start error:", err);
        }
    };

    if (startAI) startAI.addEventListener("click", handler(true));
    if (startFallback) startFallback.addEventListener("click", handler(false));
}

/* ═══════════════════════════════════════════════════════
   3. OBSERVAR DOM — respuestas y fin de partida
   ═══════════════════════════════════════════════════════ */

function observeGame() {
    const optionsEl = document.getElementById("options");

    // Watch for answer results (correct/incorrect classes)
    if (optionsEl) {
        const observer = new MutationObserver(() => {
            if (!pState.sessionActive) return;

            const buttons = optionsEl.querySelectorAll(".option-btn");
            let hasResult = false;
            let isCorrect = false;
            let selectedIdx = -1;
            let correctIdx = -1;

            buttons.forEach((btn, idx) => {
                if (btn.classList.contains("correct") && btn.classList.contains("winner")) {
                    correctIdx = idx;
                }
                if (btn.classList.contains("selected")) {
                    selectedIdx = idx;
                }
                if (
                    btn.classList.contains("correct") ||
                    btn.classList.contains("incorrect")
                ) {
                    hasResult = true;
                }
            });

            if (!hasResult) return;

            // Determine correct vs incorrect
            if (selectedIdx >= 0 && correctIdx >= 0) {
                isCorrect = selectedIdx === correctIdx;
            } else {
                // Fallback: check if selected has "correct" class
                isCorrect = buttons[selectedIdx]?.classList.contains("correct") ?? false;
            }

            // Avoid double-logging the same level
            const levelInfo = document.getElementById("level-info");
            const levelMatch = levelInfo?.textContent?.match(/(\d+)/);
            const level = levelMatch ? parseInt(levelMatch[1], 10) : pState.currentLevel + 1;

            const alreadyLogged = pState.questionsLog.some((q) => q.level === level);
            if (alreadyLogged) return;

            pState.currentLevel = level;

            if (isCorrect) {
                pState.correctCount++;
                pState.levelsEarned.push(level);
                // Extract score from level info
                const scoreMatch = levelInfo?.textContent?.match(
                    /\$\s*([0-9.,]+)/
                );
                if (scoreMatch) {
                    pState.currentScore = parseInt(
                        scoreMatch[1].replace(/[.,]/g, ""),
                        10
                    );
                }
            } else {
                pState.incorrectCount++;
            }

            pState.questionsLog.push({
                level,
                correct: isCorrect,
                selected_option: selectedIdx,
                correct_index: correctIdx,
            });
        });

        observer.observe(optionsEl, {
            childList: true,
            subtree: true,
            attributes: true,
            attributeFilter: ["class"],
        });
    }

    // Watch for game-over state (restart button becomes visible)
    const restartBtn = document.getElementById("restart-game");
    if (restartBtn) {
        const restartObserver = new MutationObserver(() => {
            if (!pState.sessionActive) return;
            if (!restartBtn.classList.contains("hidden") && !restartBtn.disabled) {
                // Game is over
                finishSession("COMPLETED");
            }
        });

        restartObserver.observe(restartBtn, {
            attributes: true,
            attributeFilter: ["class", "disabled"],
        });

        // Also intercept restart to reset session state
        restartBtn.addEventListener("click", () => {
            pState.sessionActive = false;
            pState.sessionId = null;
        });
    }
}

/* ═══════════════════════════════════════════════════════
   4. OBSERVAR COMODINES
   ═══════════════════════════════════════════════════════ */

function observeLifelines() {
    const names = ["hint", "friend", "fifty"];
    names.forEach((name) => {
        const btn = document.getElementById(name);
        if (!btn) return;

        const obs = new MutationObserver(() => {
            if (btn.classList.contains("used")) {
                pState.lifelinesUsed[name] = true;
            }
        });

        obs.observe(btn, {
            attributes: true,
            attributeFilter: ["class"],
        });
    });
}

/* ═══════════════════════════════════════════════════════
   5. ENVIAR DATOS FINALES
   ═══════════════════════════════════════════════════════ */

async function finishSession(status) {
    if (!pState.sessionId || !pState.sessionActive) return;

    pState.sessionActive = false;

    const durationMs = pState.startedAt ? Date.now() - pState.startedAt : null;

    const metadata = {
        mode: pState.mode,
        language: pState.language,
        total_questions: 15,
        last_question_level: pState.currentLevel,
        lifelines_used: { ...pState.lifelinesUsed },
        levels_earned: [...pState.levelsEarned],
        questions_summary: [...pState.questionsLog],
    };

    const payload = {
        status,
        score: pState.currentScore,
        correct_count: pState.correctCount,
        incorrect_count: pState.incorrectCount,
        duration_ms: durationMs,
        metadata,
    };

    try {
        await fetch(`${API_BASE}/sessions/${pState.sessionId}`, {
            method: "PATCH",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload),
        });
    } catch (err) {
        console.error("Session finish error:", err);
    }
}

/* ═══════════════════════════════════════════════════════
   6. BEFOREUNLOAD — marcar como ABANDONED si se cierra
   ═══════════════════════════════════════════════════════ */

function setupBeforeUnload() {
    window.addEventListener("beforeunload", () => {
        if (!pState.sessionActive || !pState.sessionId) return;

        const durationMs = pState.startedAt ? Date.now() - pState.startedAt : null;

        const payload = {
            status: "ABANDONED",
            score: pState.currentScore,
            correct_count: pState.correctCount,
            incorrect_count: pState.incorrectCount,
            duration_ms: durationMs,
            metadata: {
                mode: pState.mode,
                language: pState.language,
                total_questions: 15,
                last_question_level: pState.currentLevel,
                lifelines_used: { ...pState.lifelinesUsed },
                levels_earned: [...pState.levelsEarned],
                questions_summary: [...pState.questionsLog],
            },
        };

        // sendBeacon for reliability on page close
        navigator.sendBeacon(
            `${API_BASE}/sessions/${pState.sessionId}`,
            new Blob([JSON.stringify(payload)], { type: "application/json" })
        );
    });
}

/* ═══════════════════════════════════════════════════════
   INIT
   ═══════════════════════════════════════════════════════ */

document.addEventListener("DOMContentLoaded", () => {
    listenLanguageSwitch();
    injectRegistrationModal();
    interceptGameStart();
    observeGame();
    observeLifelines();
    setupBeforeUnload();
});
