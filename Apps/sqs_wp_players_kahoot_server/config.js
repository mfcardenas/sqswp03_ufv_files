const LLM_CONFIG = {
    enabled: true,
    baseUrl: "http://localhost:11434/api/generate",
    model: "gpt-oss",
    timeoutMs: 15000
};

const APP_CONFIG = {
    maxPlayers: 200,
    defaultTimerSeconds: 30,
    hostPasswordHint: "teachISO!"
};

if (typeof module !== "undefined") {
    module.exports = { LLM_CONFIG, APP_CONFIG };
} else {
    window.LLM_CONFIG = LLM_CONFIG;
    window.APP_CONFIG = APP_CONFIG;
}
