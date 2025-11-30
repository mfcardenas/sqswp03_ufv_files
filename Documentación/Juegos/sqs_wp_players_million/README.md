# ISOmillionaire – Instructor README

ISOmillionaire recreates the classic TV quiz format to teach ISO 9241, ISO/IEC/IEEE 29148, and ISO/IEC 25010 topics. The experience ships as a standalone SPA (static HTML/CSS/JS) with bilingual copy, lifelines, and an optional LLM pipeline for fresh questions.

## Highlights

- **Dual content sources:** Launch AI-driven rounds (Ollama `gpt-oss`) or fall back to the curated `questions_fallback.js` bank.
- **Instant bilingual UI:** Language toggle keeps UI strings, lifeline copy, and prize ladder labels synced between ES/EN.
- **Classic lifelines:** Hint, Phone a Friend, and 50/50, each with contextual explanations tied to ISO guidance.
- **Accessible layout:** Responsive CSS, ARIA labels for the prize ladder, reduced-motion hooks, and keyboard-friendly controls.
- **Dynamic prize ladder:** Instructors can dock the ranking at the right or bottom using the toggle buttons.

## Running the Game

1. Serve this folder with any static server (`python -m http.server 8080`, VS Code Live Preview, etc.).
2. Open `index.html` in a Chromium-based browser.
3. Choose **Empezar con IA** for LLM questions or **Preguntas de reserva** for the offline bank.
4. Walk the class through each level, locking answers only after students confirm their rationale.
5. Use the restart button to reset the streak and play another session.

> **Note:** If the LLM endpoint is unreachable, the UI automatically flips to fallback mode and shows a warning badge in the status pill.

## Configuration

`config.js` centralizes the gameplay knobs:

```js
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
```

Adjust `LLM_CONFIG` if your Ollama server runs on another host/port or if you prefer a different local model. Modify `moneyLadder` to change the payout curve.

## File Map

```
sqs_wp_players_million/
├── index.html            # SPA entry
├── styles.css            # JetBrains Mono + Outfit themed UI
├── config.js             # LLM + ladder config
├── questions_fallback.js # Curated ISO question bank (ES/EN)
└── game.js               # State machine, lifelines, rendering
```

## Question Sources

- **Fallback bank:** `questions_fallback.js` stores bilingual prompts grouped by ISO focus (ergonomics, requirements, product quality). Update the dataset to curate new themes.
- **LLM prompts:** `game.js` assembles a structured prompt that demands 15 tiers, ISO tags, and rationales. The loader overlay (`loading-overlay`) keeps students informed while new rounds are generated.

## Facilitation Checklist

1. **Pre-session:** Verify the LLM endpoint, test both languages, and pick the desired ladder placement.
2. **During play:** Encourage students to discuss the rationale before clicking **Responder**. Use lifelines sparingly to introduce real ISO trade-offs.
3. **After each question:** Highlight the explanation text to connect the answer with the relevant ISO clause.
4. **Wrap-up:** Celebrate the furthest level reached, capture improvement ideas, and optionally export the chat log/notes.

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| Buttons stay disabled | Ensure at least one answer option is selected before pressing **Responder**. |
| No response from AI mode | Confirm Ollama is running and reachable; otherwise use fallback mode. |
| Ladder overlaps content | Use the ladder toggle to move it to the bottom on small resolutions. |
| Language does not switch | Hard refresh the browser (`Ctrl+Shift+R`); service workers are not used, so cache issues are minimal. |

## License

Same licensing terms as the parent repository (`sqswp035_iso_ufv_new`).