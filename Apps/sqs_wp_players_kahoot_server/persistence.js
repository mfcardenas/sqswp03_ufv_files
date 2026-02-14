/**
 * persistence.js — Client-side persistence for ISO Kahoot
 * --------------------------------------------------------
 * Loaded in player.html / player_en.html AFTER player.js.
 * Shows a registration modal (nickname + university), saves to localStorage,
 * registers via POST /api/players.
 *
 * player.js reads from localStorage to include userId + university
 * in the player:joinSession event automatically.
 */
(() => {
    /* ── i18n ─────────────────────────────────────────── */
    const LANG_DICT = {
        es: {
            modalTitle: "Registro de jugador",
            nicknameLabel: "Apodo / Nickname",
            nicknamePlaceholder: "Tu nombre",
            universityLabel: "Universidad",
            universityPlaceholder: "Ej: UFV",
            submitBtn: "Registrarse",
            errorRequired: "Completa ambos campos.",
            errorServer: "Error registrando jugador. Intenta de nuevo.",
            badgeLogout: "Cerrar sesión",
            badgeTooltip: "Clic para cerrar sesión"
        },
        en: {
            modalTitle: "Player Registration",
            nicknameLabel: "Nickname",
            nicknamePlaceholder: "Your name",
            universityLabel: "University",
            universityPlaceholder: "e.g. UFV",
            submitBtn: "Register",
            errorRequired: "Please fill in both fields.",
            errorServer: "Error registering player. Try again.",
            badgeLogout: "Log out",
            badgeTooltip: "Click to log out"
        }
    };

    const getCurrentLang = () =>
        (document.body?.dataset?.uiLang === "en") ? "en" : "es";

    const t = (key) => LANG_DICT[getCurrentLang()]?.[key] || key;

    /* ── Local storage helpers ────────────────────────── */
    const STORAGE_KEY = "isoKahootPlayer";

    const getStoredPlayer = () => {
        try {
            return JSON.parse(localStorage.getItem(STORAGE_KEY));
        } catch { return null; }
    };

    const setStoredPlayer = (data) => {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(data));
    };

    const clearStoredPlayer = () => {
        localStorage.removeItem(STORAGE_KEY);
    };

    /* ── Player badge ─────────────────────────────────── */
    const injectBadge = (nickname, university) => {
        if (document.getElementById("persist-badge")) return;
        const header = document.querySelector("header");
        if (!header) return;

        const badge = document.createElement("div");
        badge.id = "persist-badge";
        badge.title = t("badgeTooltip");
        badge.style.cssText = `
            position: absolute; top: 10px; right: 14px;
            display: flex; align-items: center; gap: 8px;
            background: rgba(255,255,255,0.12);
            border: 1px solid rgba(255,255,255,0.2);
            border-radius: 8px; padding: 6px 14px;
            color: #fff; font-size: 0.85rem; cursor: pointer;
            backdrop-filter: blur(6px);
            z-index: 1000;
            transition: background 0.2s;
        `;
        badge.innerHTML = `
            <span>👤 <strong>${nickname}</strong> · ${university}</span>
            <button id="persist-logout" style="
                background: none; border: none; color: #f87171;
                cursor: pointer; font-size: 0.8rem; padding: 2px 6px;
            ">${t("badgeLogout")}</button>
        `;
        badge.addEventListener("mouseenter", () => badge.style.background = "rgba(255,255,255,0.2)");
        badge.addEventListener("mouseleave", () => badge.style.background = "rgba(255,255,255,0.12)");
        header.style.position = "relative";
        header.appendChild(badge);

        document.getElementById("persist-logout").addEventListener("click", (e) => {
            e.stopPropagation();
            clearStoredPlayer();
            badge.remove();
            // Re-enable nickname input
            const nicknameInput = document.querySelector("#player-form input[name='nickname']");
            if (nicknameInput) { nicknameInput.readOnly = false; nicknameInput.style.opacity = "1"; nicknameInput.value = ""; }
            showModal();
        });
    };

    /* ── Registration modal ───────────────────────────── */
    const showModal = () => {
        if (document.getElementById("persist-modal-overlay")) return;

        const overlay = document.createElement("div");
        overlay.id = "persist-modal-overlay";
        overlay.style.cssText = `
            position: fixed; inset: 0;
            background: rgba(0,0,0,0.65);
            display: flex; align-items: center; justify-content: center;
            z-index: 9999;
            backdrop-filter: blur(4px);
        `;

        const modal = document.createElement("div");
        modal.style.cssText = `
            background: #1e1e2e; color: #f0f0f0;
            border-radius: 14px; padding: 32px;
            max-width: 380px; width: 90%;
            box-shadow: 0 12px 40px rgba(0,0,0,0.5);
            font-family: 'Outfit', sans-serif;
        `;
        modal.innerHTML = `
            <h2 style="margin:0 0 20px; text-align:center; font-size:1.3rem;">
                ${t("modalTitle")}
            </h2>
            <label style="display:block; margin-bottom:14px;">
                <span style="font-size:0.85rem; color:#a0a0b0;">${t("nicknameLabel")}</span>
                <input id="persist-nickname" type="text" placeholder="${t("nicknamePlaceholder")}"
                    style="width:100%;box-sizing:border-box;padding:10px 12px;margin-top:4px;
                    border:1px solid #444;border-radius:8px;background:#2a2a3e;color:#fff;
                    font-size:1rem;outline:none;" />
            </label>
            <label style="display:block; margin-bottom:20px;">
                <span style="font-size:0.85rem; color:#a0a0b0;">${t("universityLabel")}</span>
                <input id="persist-university" type="text" placeholder="${t("universityPlaceholder")}"
                    style="width:100%;box-sizing:border-box;padding:10px 12px;margin-top:4px;
                    border:1px solid #444;border-radius:8px;background:#2a2a3e;color:#fff;
                    font-size:1rem;outline:none;" />
            </label>
            <button id="persist-submit" style="
                width:100%;padding:12px;border:none;border-radius:8px;
                background:linear-gradient(135deg,#6366f1,#8b5cf6);
                color:#fff;font-size:1rem;font-weight:600;cursor:pointer;
                transition:opacity 0.2s;
            ">${t("submitBtn")}</button>
            <p id="persist-error" style="color:#f87171;font-size:0.85rem;text-align:center;margin-top:10px;min-height:1.2em;"></p>
        `;

        overlay.appendChild(modal);
        document.body.appendChild(overlay);

        document.getElementById("persist-submit").addEventListener("click", handleRegister);
        document.getElementById("persist-nickname").addEventListener("keydown", (e) => {
            if (e.key === "Enter") document.getElementById("persist-university").focus();
        });
        document.getElementById("persist-university").addEventListener("keydown", (e) => {
            if (e.key === "Enter") handleRegister();
        });
    };

    const handleRegister = async () => {
        const nickname = document.getElementById("persist-nickname").value.trim();
        const university = document.getElementById("persist-university").value.trim();
        const errorEl = document.getElementById("persist-error");

        if (!nickname || !university) {
            errorEl.textContent = t("errorRequired");
            return;
        }

        const btn = document.getElementById("persist-submit");
        btn.disabled = true;
        btn.style.opacity = "0.6";
        errorEl.textContent = "";

        try {
            const res = await fetch("/api/players", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ nickname, university })
            });
            const data = await res.json();
            if (!res.ok || !data.ok) {
                throw new Error(data.error || "Unknown error");
            }
            setStoredPlayer({ userId: data.userId, nickname, university });

            // Remove modal
            const overlay = document.getElementById("persist-modal-overlay");
            if (overlay) overlay.remove();

            // Show badge + pre-fill nickname
            injectBadge(nickname, university);
            prefillPlayerForm(nickname);

        } catch (err) {
            errorEl.textContent = t("errorServer");
            btn.disabled = false;
            btn.style.opacity = "1";
        }
    };

    /* ── Pre-fill nickname in the game's join form ────── */
    const prefillPlayerForm = (nickname) => {
        const nicknameInput = document.querySelector("#player-form input[name='nickname']");
        if (nicknameInput) {
            nicknameInput.value = nickname;
            nicknameInput.readOnly = true;
            nicknameInput.style.opacity = "0.7";
        }
    };

    /* ── Initialization ───────────────────────────────── */
    const init = () => {
        const stored = getStoredPlayer();
        if (stored && stored.userId && stored.nickname) {
            injectBadge(stored.nickname, stored.university);
            prefillPlayerForm(stored.nickname);
        } else {
            showModal();
        }
    };

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", init);
    } else {
        init();
    }
})();
