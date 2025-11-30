# ISO 9241 Usability Quest

Single-page learning experience that helps instructors guide students through ISO 9241 usability challenges. The UI is in English, while facilitation notes can be exchanged in Spanish during class.

## Getting started

1. Open the folder `sqs_wp_ux_players_9241` with a static server (VS Code Live Preview, `python -m http.server`, etc.).
2. Load `index.html` in the browser.
3. Choose a content source:
   - **Static JSON**: uses `data/iso9241_challenges.json` for deterministic labs.
   - **Dynamic (Ollama gpt-oss)**: fetches fresh content from `http://localhost:11434/api/generate`. Ensure Ollama runs locally and exposes the `gpt-oss` model.
4. If you stay offline, pick one of the available static scenarios (Usability Quest, Guided Onboarding Sprint, Field Validation Expedition) from the drop-down.
5. Press **Load Scenario**. Review the intro screen con el grupo y, cuando estén listos, inicien los laboratorios desde la propia interfaz.

## Project structure

```
├── index.html                # entry point
├── assets/
│   └── css/main.css          # visual layer
├── data/
│   ├── iso9241_challenges.json         # baseline scenario
│   ├── iso9241_guided_onboarding.json  # onboarding-focused scenario
│   └── iso9241_field_validation.json   # field validation scenario
├── docs/
│   └── update-json-prompt.md # instructions to refresh JSON via AI
├── src/
│   ├── data/content-provider.js  # fetches JSON or Ollama content
│   ├── main.js                   # orchestrates rendering and state changes
│   ├── state/
│   │   ├── scoring.js
│   │   └── session-store.js
│   ├── ui/
│   │   ├── intro-screen.js
│   │   ├── lab-runner.js
│   │   └── results-screen.js
│   └── utils/dom.js
└── README.md
```

## Content refresh workflow

- Update any of the JSON files under `data/` manually or by following `docs/update-json-prompt.md`.
- The file must follow the schema referenced in `src/data/content-provider.js`.
- No build tools are required; reload the browser to pick up changes.

## Browser support

Tested with current versions of Chrome and Edge. Because the app uses `fetch` for local files, serve the directory over HTTP instead of opening `index.html` via `file://`.
