# ISO 9241 Usability Quest – README

ISO 9241 Usability Quest is a browser-based lab environment that turns human-centred design principles into interactive workshops. This folder mirrors the build shipped in `Documentación/Juegos/sqs_wp_ux_players_9241`.

## Experience Highlights

- **Three curated labs:** Discovery Workshop, Interaction Audit, and Validation Sprint—each mapped to ISO 9241-110/112/210/11 clauses.
- **Dynamic expansion:** Optional Ollama (`gpt-oss`) integration that generates fresh labs while respecting the same schema as the static JSON files.
- **Guided artefacts:** On-demand Markdown templates (storyboards, observation logs, ISO checklists) to support each challenge.
- **Scoring + debrief:** Automatic score out of 100 plus insight cards to guide instructor-led retrospectives.
- **Bilingual facilitation:** UI copy in English; instructors can mix Spanish explanations without affecting flow.

## Quick Start

1. Serve this directory with a static server (`python -m http.server 9000`, VS Code Live Preview, etc.).
2. Visit the served URL and load `index.html` (avoid `file://`).
3. Select **Static JSON** for deterministic labs or **Dynamic (Ollama gpt-oss)** to request new content (ensure Ollama is running locally).
4. Choose the scenario from the dropdown, press **Load Scenario**, and review the intro slide with the class.
5. Walk through each challenge, logging decisions and quiz answers inside the SPA.
6. Use the generated score to wrap up, highlight clause coverage, and assign follow-up work.

> **Need a quick Ollama check?** Run `ollama run gpt-oss` in a separate terminal before using the dynamic option.

## File Map

```
sqs_wp_ux_players_9241/
├── index.html
├── assets/
│   └── css/main.css
├── data/
│   ├── iso9241_challenges.json
│   ├── iso9241_guided_onboarding.json
│   └── iso9241_field_validation.json
├── docs/
│   ├── update-json-prompt.md
│   └── templates/
│       ├── context-brief-template.md
│       ├── interaction-flow-matrix.md
│       ├── observation-log-template.md
│       ├── onboarding-friction-log-template.md
│       ├── …
├── src/
│   ├── data/content-provider.js
│   ├── main.js
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

## Dynamic Content Contract

- Endpoint: `http://localhost:11434/api/generate`
- Model: `gpt-oss` (change inside `src/data/content-provider.js` if needed)
- Timeout: 15 s (constant `OLLAMA_TIMEOUT_MS`)

Generated labs must contain:

1. Three lab blocks (`lab-a`, `lab-b`, `lab-c`) focusing on discovery, interaction assessment, and validation respectively.
2. Five challenges per lab with objectives, 4–6 tasks, at least two quizzes, and helper references (`helperText`, `helperMd`, or resource IDs).
3. ISO clause tags so instructors can reference standards during the discussion.
4. A score descriptor (e.g., `{ "perCorrect": 20, "max": 100 }`) plus a completion summary.

If the request fails, the SPA reverts to the last selected static scenario and raises a warning pill in the header.

## Customization

| Need | Action |
| --- | --- |
| Add/modify labs | Edit the JSON files under `data/` while keeping the schema (labs → challenges → tasks/quizzes). |
| Update prompts | Follow `docs/update-json-prompt.md` to regenerate datasets with AI or adjust the inline prompt in `content-provider.js`. |
| Extend resources | Drop new Markdown templates into `docs/templates/` and reference them from your JSON via `helperMd`. |
| Change scoring weights | Modify `src/state/scoring.js` to increase/decrease per-challenge value or end-of-lab bonuses. |
| Rebrand UI | Override CSS variables in `assets/css/main.css` (colors, spacing, typography). |

## Facilitation Flow

1. **Context briefing:** Introduce personas, platforms, and ISO 9241 clauses in focus.
2. **Challenge walkthrough:** Read each objective, let students inspect helper material, and capture the agreed answer.
3. **Evidence review:** Open the linked Markdown templates (observation logs, impact-effort matrices, etc.) to ground the discussion.
4. **Score interpretation:** Use the final score + insight cards to highlight strengths and improvement areas.
5. **Follow-up:** Export notes (copy/paste), assign homework, or feed the findings into the next sprint.

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| Template modal blank | Check the `helperMd` path inside the JSON; ensure the file exists under `docs/templates/`. |
| Fetch error on load | Serve via HTTP—double-clicking `index.html` blocks `fetch` for local files. |
| Dynamic labs stuck on loading | Confirm Ollama is running and reachable; watch its terminal for prompt errors. |
| Score never updates | Ensure each quiz has at least one answer recorded; unanswered quizzes keep the score at 0. |

## License

This documentation bundle inherits the license defined in the parent repository (`sqswp035_iso_ufv_new`). Content © ISO WP Lab (UFV).*** End Patch
