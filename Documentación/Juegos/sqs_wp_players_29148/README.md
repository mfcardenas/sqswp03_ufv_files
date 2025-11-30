# ISO 29148 Requirements Players

Single-page classroom app to help instructors run ISO/IEC/IEEE 29148 workshops. Students load curated scenarios or ask a local Ollama instance (gpt-oss) to generate fresh requirement labs while keeping the exact schema required by the UI.

## Getting started

1. Serve `sqs_wp_players_29148` with any static server (`python -m http.server`, VS Code Live Preview, etc.).
2. Open `index.html` in your browser.
3. Pick **Static JSON** for deterministic scenarios or **Dynamic (Ollama gpt-oss)** for AI-generated content.
4. For static mode, choose one of the available scenarios (Requirements Rally or Supplier Alignment) and press **Load Scenario**.
5. Review the intro screen with the cohort, then walk through each challenge, recording quiz answers and opening resources directly from the modal viewer.

## Project structure

```
├── index.html
├── assets/
│   └── css/main.css
├── data/
│   ├── iso29148_requirements_rally.json
│   └── iso29148_supplier_alignment.json
├── docs/
│   ├── templates/*.md
│   └── update-json-prompt.md
├── src/
│   ├── data/
│   │   ├── content-provider.js
│   │   └── static-options.js
│   ├── state/
│   │   ├── scoring.js
│   │   └── session-store.js
│   ├── ui/
│   │   ├── intro-screen.js
│   │   ├── lab-runner.js
│   │   ├── resource-preview.js
│   │   └── results-screen.js
│   └── utils/dom.js
└── README.md
```

## Dynamic content (Ollama)

If you select **Dynamic (Ollama gpt-oss)** the app calls `http://localhost:11434/api/generate` with a strict prompt that enforces:

- Three labs (`lab-a`, `lab-b`, `lab-c`) covering elicitation, specification, and validation
- Five challenges with objectives, 4–6 tasks, and at least two quizzes
- Tasks that always include helper material (examples, checklists, or resources)
- Scoring payload (`{"perCorrect":20,"max":100}`) plus a completion message

Failures to reach Ollama fall back to the static scenario so the class can continue.

## Browser support

Tested with the latest Chrome and Edge. Because the app uses `fetch` for local JSON and Markdown, run it through `http://` instead of `file://` to avoid CORS/file permission issues.
