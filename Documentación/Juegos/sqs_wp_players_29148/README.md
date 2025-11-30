# ISO 29148 Requirements Players – README

ISO 29148 Requirements Players is a facilitator-first SPA that turns requirements engineering labs into live classroom sessions. This folder mirrors the build deployed in `Documentación/Juegos/sqs_wp_players_29148`.

## What’s Included

- **Two curated labs:** Requirements Rally and Supplier Alignment, fully scripted with KPIs, stakeholder roles, quizzes, and wrap-up copy.
- **Dynamic generation:** Optional Ollama (`gpt-oss`) integration that produces three fresh labs (`lab-a`, `lab-b`, `lab-c`) on demand using a strict schema.
- **Embedded resources:** Markdown templates (briefs, matrices, validation logs) that open inline so students never leave the SPA.
- **Scoring + feedback:** Automated 0–100 score plus localized recommendations for the final debrief.

## Quick Start

1. Serve this directory with a static server (`python -m http.server 8000`, VS Code Live Preview, etc.).
2. Open `index.html` from the served URL (avoid `file://` to keep fetch/Markdown working).
3. Choose a content source:
	- **Static JSON:** Deterministic labs from `data/`. Pick your scenario and click **Load Scenario**.
	- **Dynamic (Ollama gpt-oss):** Ensure Ollama runs locally and exposes the `gpt-oss` model, then request new labs.
4. Review the intro slide with the cohort, then work through each challenge by capturing student answers in the UI.
5. Use the scorecard and completion message to drive the retrospective.

> **Tip:** Keep DevTools open during rehearsal—helper logs reveal how payloads are parsed and validated.

## File Map

```
sqs_wp_players_29148/
├── index.html
├── assets/
│   └── css/main.css
├── data/
│   ├── iso29148_requirements_rally.json
│   └── iso29148_supplier_alignment.json
├── docs/
│   ├── update-json-prompt.md
│   └── templates/
│       ├── acceptance-criteria-template.md
│       ├── change-impact-canvas.md
│       ├── context-of-use-worksheet.md
│       ├── …
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

## Dynamic Content Requirements

| Setting | Value |
| --- | --- |
| Endpoint | `http://localhost:11434/api/generate` |
| Model | `gpt-oss` (change in `content-provider.js` if needed) |
| Timeout | 15 s (`OLLAMA_TIMEOUT_MS`) |

The runtime enforces:

- Three labs with IDs `lab-a`, `lab-b`, `lab-c` covering elicitation, specification, and validation.
- Five challenges per lab, each holding objectives, 4–6 tasks, ≥2 quizzes, and helper resources (examples, checklists, Markdown).
- Scoring payload such as `{ "perCorrect": 20, "max": 100 }` plus a completion summary string.
- Graceful fallback to the last selected static lab if the LLM call fails.

## Customization

| Goal | Where |
| --- | --- |
| Update static scenarios | Edit the JSON files in `data/` (ensure you keep IDs, titles, challenges arrays, and helper references intact). |
| Refresh prompts | Follow `docs/update-json-prompt.md` to regenerate datasets via AI, or tweak the `OLLAMA_PROMPT` constant inside `content-provider.js`. |
| Add more resources | Drop Markdown files into `docs/templates/` and reference them from JSON via `"helperMd": "docs/templates/..."`. |
| Adjust scoring | Modify the weights inside `src/state/scoring.js` (per quiz, completion bonus, etc.). |
| Rebrand visuals | Override CSS variables in `assets/css/main.css` (primary, accent, background, typography). |

## Classroom Flow

1. **Kick-off:** Explain the chosen lab’s context, actors, and ISO clauses in focus.
2. **Challenge loop:** For each challenge, students analyze objectives, discuss options, and vote on the best answer while you record it in the UI.
3. **Resource dives:** Open the referenced Markdown template (traceability matrix, validation protocol, etc.) for hands-on guidance.
4. **Score review:** After the last challenge, discuss the score, automated feedback, and suggested improvements.
5. **Wrap-up:** Capture the learning outcomes in your LMS or shared notes and plan follow-up work if needed.

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| Blank screen after load | Confirm you are serving via HTTP; fetch calls fail when loaded with `file://`. |
| Markdown modal shows 404 | Validate the `helperMd` path in the JSON file matches a real template. |
| Dynamic labs never finish | Check the Ollama terminal for prompt errors; run `ollama run gpt-oss` manually to verify availability. |
| Score remains 0 | Ensure each quiz has an answer recorded; unanswered quizzes provide 0 weight. |

## License

This bundle inherits the license from the root repository (`sqswp035_iso_ufv_new`). Content © ISO WP Lab (UFV).*** End Patch
