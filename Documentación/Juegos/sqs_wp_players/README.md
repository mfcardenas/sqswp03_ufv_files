# ISO Laboratory – Game Master Handbook

ISO Laboratory is a classroom-ready simulator that blends narrative decision trees, ISO-standard quizzes, and management dashboards so instructors can illustrate ISO 9241, ISO/IEC/IEEE 29148, and ISO/IEC 25010 without slides. This build mirrors the public documentation bundle under `Documentación/Juegos/sqs_wp_players`.

## Experience Overview

| Mode | Entry point | Purpose |
| --- | --- | --- |
| **ISO Laboratory (wizard)** | `index.html` | Guided onboarding + decision engine with XP, levels, and achievements. |
| **ISO Quiz Module** | `iso-index.html` | Lightweight quiz launcher ideal for timed checkpoints. |
| **ISO Real / ISO Real EN** | `iso-real.html` / `iso-real-en.html` | Narrative-driven decision boards with bilingual UI and synchronized styles. |
| **MedCore Hospital Scenario** | `proyecto-medcore/medcore-enhanced-game*.html` | Critical-system simulation focused on healthcare compliance. |

Each mode shares the same storyline assets, scoring widgets, and ISO-aligned prompts, so you can switch depending on the classroom tempo.

## Key Learning Goals

- Map every decision to at least one ISO 25010 characteristic (functionality, reliability, usability, security, performance, maintainability, portability, compatibility).
- Practice ISO/IEC/IEEE 29148 traceability by forcing students to justify trade-offs before submission.
- Reinforce ISO 9241 ergonomics through UI/UX remediation challenges.
- Encourage reflection with auto-generated feedback blocks after every scenario.

## Feature Highlights

- **Scenario diversity:** Four baseline projects (e-commerce, hospital, fintech, social) plus the MedCore branch for regulated environments.
- **Gamified progression:** XP, levels, badges, and streak bonuses stored in `localStorage` per browser.
- **Randomized events:** Optional twists (scope creep, audits, breaches) to keep cohorts engaged.
- **Accessibility-first UI:** Keyboard navigation, WCAG AA contrast, and motion-reduce hooks built into `game-styles.css` and `wizard.css`.
- **Bilingual parity:** `iso-real-en.html` + `iso-real-game-en.js` mirror the Spanish assets.

## Quick Start

1. Launch a static server from this folder (e.g. `python -m http.server 8080`).
2. Visit the mode you want to facilitate (`index.html`, `iso-index.html`, etc.).
3. Share the projector view with the class and read the briefing together.
4. Let students propose decisions; log the final choice inside the UI.
5. Debrief the automatic feedback, metrics impact, and XP changes.

> **Tip:** Keep the browser console open while testing; helper logs describe how each decision impacts ISO metrics.

## File Map

```
sqs_wp_players/
├── index.html                # Wizard entry point
├── script.js                 # Legacy helpers used by index.html
├── game.js                   # Core game loop (XP, decisions, random events)
├── game-styles.css
├── styles.css                # Base styles shared across pages
├── wizard.css                # Tutorial + onboarding visuals
├── iso-index.html            # Quiz-only entry
├── iso-quiz-module.js        # ES module powering Spanish quiz mode
├── iso-quiz-module-en.js     # English quiz copy
├── iso-real.html             # Spanish narrative simulator
├── iso-real-game.js          # Logic for ISO Real Spanish
├── iso-real-styles.css
├── iso-real-en.html          # English narrative simulator
├── iso-real-game-en.js
├── iso-real-styles-en.css
└── proyecto-medcore/
    ├── medcore-enhanced-game.html
    ├── medcore-enhanced-game-en.html
    ├── medcore-enhanced-styles.css
    ├── medcore-enhanced-styles-en.css
    └── bck/                  # Archived prototypes
```

## Customization Notes

- **Scenario texts:** Edit the arrays inside `game.js` (search for `SCENARIOS`) to tweak narratives or add more decision nodes.
- **ISO metrics tuning:** Adjust the scoring tables near the top of `game.js` or `iso-real-game*.js` to prioritize different quality characteristics.
- **Language copy:** Update `iso-real-game-en.js` or `iso-quiz-module-en.js` to keep both locales in sync.
- **MedCore branding:** Override the CSS variables in `medcore-enhanced-styles*.css` to match institutional colors.

## Facilitation Flow

1. **Briefing:** Present the project charter. Highlight which ISO standard is under evaluation.
2. **Decision rounds:** Students vote or pitch arguments. The instructor selects the agreed option.
3. **Instant feedback:** Read the generated tips, metrics deltas, and XP with the class.
4. **Reflection:** Capture lessons learned (whiteboard, LMS, or the provided feedback text).
5. **Next scenario:** Progress through levels until you reach the final audit or release.

## Troubleshooting

| Issue | Fix |
| --- | --- |
| Fonts or icons look off | Ensure the session is served over HTTP/HTTPS so Google Fonts can load. |
| Progress does not persist | Check that the browser allows localStorage (no incognito restrictions). |
| Styles look broken in ISO Real EN | Verify `iso-real-styles-en.css` is loaded (hard refresh with `Ctrl+Shift+R`). |
| MedCore appears in Spanish only | Use `medcore-enhanced-game-en.html` for the English deck. |

## License & Credits

This distribution inherits the licensing terms from the main `sqswp035_iso_ufv_new` repository. Content authored by the ISO WP lab team (UFV).