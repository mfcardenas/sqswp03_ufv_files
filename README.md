# Workspace Overview

This workspace consolidates every deliverable used in the ISO-driven Software Engineering curriculum: production-ready web apps, public documentation bundles, GPT guides, hands-on labs, classroom practices, and workshop packets. Use this README as the map to understand what lives where before deploying or editing anything.

## Top-Level Layout

| Path | Purpose |
| --- | --- |
| `.vscode/` | Editor settings, launch configs, and recommended extensions for this workspace. |
| `Apps/` | Source code for every interactive game or service (ISO Laboratory, ISOmillionaire, host/player quiz, etc.) plus zipped hand-off builds. |
| `Documentación/` | Standalone website that exposes all games, labs, and ISO explanations for public hosting. Includes its own navigation and README. |
| `GPTs/` | Prompt guides, delivery notes, and READMEs for the three GPT assistants (ExamGPT-UFV, ConsultorLabISO, ISOQuest). |
| `Laboratorios/` | Canonical lab content organized by ISO standard (9241, 29148, 25010:2023) with bilingual HTML pages, assets, and per-lab READMEs. |
| `Prácticas/` | Practice packets in DOCX format for Spanish (ES) and English (EN) cohorts. |
| `Talleres/` | Workshop slide decks and facilitator docs for Ingeniería del Software I. |

The remainder of this document drills into each folder.

## Apps/

Interactive applications live here. Highlights:

- `sqswp035_iso_ufv_new/` – Monorepo with backend services (`llm_game_server.py`, `usability_universe_server.py`), container tooling, docs, and two frontends under `iso_standards_games/`.
- `sqs_wp_players/` – Original ISO Laboratory SPA with multiple entry points (`index.html`, `iso-index.html`, ISO Real bilingual modes, MedCore scenario) and shared CSS/JS assets.
- `sqs_wp_players_29148/` – Requirements Players SPA plus `docs/templates/` for resource overlays.
- `sqs_wp_players_million/` – ISOmillionaire ladder game (hybrid AI/fallback questions).
- `sqs_wp_players_kahoot/` – Node/Express/Socket.IO host-player quiz app with bilingual pages, `server.js`, and Dockerfile. Includes the generated `README.md` you requested.
- `sqs_wp_ux_players_9241/` – ISO 9241 Usability Quest SPA mirroring the structure of the 29148 build.
- `WP_35.zip` and `sqs_wp_players_kahoot.zip` – Distribution bundles ready for delivery when a clean snapshot is needed.

Each subdirectory contains its own README describing setup, architecture, and facilitation flow.

## Documentación/

Static website meant for public hosting:

- Landing pages: `index.html` / `index_es.html` / `index_en.html` switch between English and Spanish views.
- `Juegos/` mirrors the playable builds so they can be launched from the documentation site without touching the source apps.
- `Laboratorios/` reproduces the ISO lab portals (9241, 29148, 25010) with bilingual indices.
- `README.md` explains how to deploy the documentation bundle and lists every embedded asset.

Use this bundle when you need a self-contained showcase without spinning up Node/Express services.

## GPTs/

Prompt libraries and reference notes for three custom GPTs:

- `ConsultorLabISO-WP35-UFV/` – Contains EN/ES DOCX prompt packs and a README describing usage scenarios.
- `ExamGPT-UFV/` – Assessment-oriented prompt sheets.
- `ISOQuest-UFV/` – Exploration-oriented guide.

These folders are primarily documentation; there is no executable code. Update them when GPT prompt templates change.

## Laboratorios/

Authoritative source for every lab handout:

- `ISO_9241_Labs/` – Split into `English/` and `Español/` trees, each with lab HTML, media, and index files plus localized READMEs.
- `ISO_IEC_IEEE_29148_Labs/` – Mirrors the bilingual structure; each lab subfolder includes slides, exercises, and README guidance.
- `ISOIEC_25010_2023_Labs/` – Latest quality-model labs with both Spanish and English content.
- `.dist/` – Build artifacts or helper scripts used when exporting the labs.

Whenever the apps reference lab content, they pull from this directory.

## Prácticas/

Practice worksheets for students:

- `ES/` and `EN/` contain DOCX files (e.g., `MT001_EN - Actividad_01_v0.0.1.docx`, integration exercises, presentations). Use these as printable or LMS-ready assignments.

## Talleres/

Workshop materials for Engineering courses:

- `Ingeniería del Software I/` stores PDFs and DOCX packs. The `Introducción a la Ingeniería del Software/` subfolder includes facilitator notes, materials lists, and activity breakdowns (`Talleres_ES_IS_Unit_01_01_*.docx`).

## Editor Settings (.vscode/)

Holds workspace-specific configuration (settings, extensions, launch configurations). Update this folder when you need to share recommended tooling with collaborators.

## Working Tips

- Treat each major folder as an independent deliverable; most ship with their own README or deployment guide.
- When preparing public demos, copy content from `Documentación/` or the zipped bundles instead of the source folders.
- For code changes, work inside `Apps/` and sync documentation in `Documentación/` once features stabilize.
- Keep DOCX-based assets versioned by naming (already v0.0.1). Avoid editing them without bumping the filename.

With this map you can onboard new collaborators faster, decide what to deploy, and locate every supporting artifact across the Material Didáctico workspace.
