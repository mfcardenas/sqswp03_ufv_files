# ISO Standards Live Quiz (Kahoot-style Host/Player)

This app delivers a real-time quiz experience inspired by Kahoot, with a password-protected teacher console and a streamlined player view. It is the live version of the experience referenced in `Documentación/Juegos` and is meant to run as a Node.js + Socket.IO service.

## Highlights

- **Dedicated roles:** `host.html` for instructors (desktop) and `player.html` for students (mobile-friendly). English counterparts (`host_en.html`, `player_en.html`) load automatically translated copy.
- **Session security:** Hosts must enter the configured password (`teachISO!` by default inside `config.js`). Codes are unique per session, and players cannot access host tools.
- **Language sync:** Host language preference is stored in `localStorage` and propagated to every connected player so questions always match the selected locale.
- **Flexible question sources:** Instructors can select predefined ISO quizzes or request new ones via LLM-backed generators (when available in `games.js`).
- **Accessibility:** Keyboard-friendly buttons, ARIA labels for live status, and responsive CSS tailored to classroom use.

## Project Structure

```
sqs_wp_players_kahoot/
├── server.js            # Express + Socket.IO backend
├── client.js            # Shared Socket.IO client helpers
├── host.js              # Host UI logic (ES)
├── host_en.html/.js     # English host surface
├── player.js            # Player UI logic (shared)
├── games.js             # Question presets + catalog metadata
├── config.js            # LLM + app configuration (also exposed client-side)
├── styles.css           # Shared styling for host/player
├── index.html           # Landing page (ES)
├── index_en.html        # Landing page (EN)
├── Dockerfile           # Container build
├── package.json         # Node dependencies (Express, Socket.IO, uuid, etc.)
└── README.md            # This file
```

## Configuration

Edit `config.js` to adjust core behavior:

```js
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
```

- Change `hostPasswordHint` (and the actual password via the `HOST_PASSWORD` env var) before deploying.
- Toggle `LLM_CONFIG.enabled` if you only plan to use curated quizzes.
- Update `defaultTimerSeconds` to adapt the rhythm of each round.

## Local Setup

```powershell
# 1) Install dependencies
yarn install   # or npm install

# 2) Run the server
yarn start     # defaults to http://localhost:3000

# 3) Open the host view
http://localhost:3000/host.html

# 4) Students join via player page
http://localhost:3000/player.html
```

Use the English endpoints (`host_en.html`, `player_en.html`) if your session runs entirely in English.

## Gameplay Flow

1. **Unlock:** Host enters the password and gains access to the control panel.
2. **Configure session:** Fill in title, context, ISO focus, number of questions, timer, and language. Choose either **IA/LLM** or **Juego predefinido**.
3. **Create session:** Click **Crear sesión** to generate a code. Share the code with students.
4. **Load content:** Use **Generar con IA** (if enabled) or **Usar juego predefinido** to load questions into the session.
5. **Manage rounds:** Buttons let you start the session, launch questions, close answers, and reveal rankings. The timer and live status update every player automatically.
6. **Wrap up:** End the session to lock responses and reset the lobby for the next class.

## Security & Data Notes

- Sessions live entirely in memory; restarting the server resets all codes and players.
- Host authentication uses in-process verification (`HOST_PASSWORD`). Use HTTPS and a strong password when deploying publicly.
- Player data is limited to nickname, score, and answer timestamps. No personal info is stored.

## Customization Tips

- **New question banks:** Extend `games.js` with additional ISO scenarios, ensuring each entry includes metadata (title, description, language, questions array).
- **Branding:** Update `styles.css` (colors, logos) and the hero sections in `index*.html` for institutional identity.
- **LLM prompts:** If you connect to a remote LLM, adjust `games.js` or the backend routes that orchestrate dynamic content to match the provider’s API.
- **Player safeguards:** `player.js` already strips navigation links; add further restrictions (e.g., rate limiting) inside `server.js` if needed.

## Troubleshooting

| Issue | Fix |
| --- | --- |
| Host buttons stay disabled | Ensure a session is created and questions are loaded; buttons enable contextually. |
| Players see old sessions | `server.js` removes socket IDs from previous rooms, but force refresh the browser if someone stayed dormant for long. |
| Language mismatch | Hosts should set language before creating the session; stored preference persists per browser profile. |
| Socket errors | Verify the server is running on the expected port and no firewall blocks WebSocket traffic. |

## License

This module inherits licensing from the root repository (`sqswp035_iso_ufv_new`). Content © ISO WP Lab (UFV).
