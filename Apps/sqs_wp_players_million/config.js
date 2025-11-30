export const LLM_CONFIG = {
    enabled: true,
    baseUrl: "http://localhost:11434/api/generate",
    model: "gpt-oss",
    timeoutMs: 15000
};

export const GAME_CONFIG = {
    totalQuestions: 15,
    defaultLanguage: "ES",
    moneyLadder: [100, 200, 300, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 125000, 250000, 500000, 1000000]
};
