# ISO Kahoot Live Quiz — Persistence Server

> 🇪🇸 [Leer en español](./README.md)

Express + Socket.IO server with PostgreSQL persistence that records every player's game attempt, including detailed per-question answers for learning analytics.

## Architecture

```
server.js               → Express + Socket.IO (game logic + persistence)
persistence-bridge.js   → Direct functions → INSERT/UPDATE game_attempts
persistence.js          → Registration modal (client-side, player.html)
db.js                   → PostgreSQL connection pool
config.js               → Configuration (LLM, timers, password)
games.js                → Predefined games (5 sets × 6 questions)
styles.css              → Shared styles
```

---

## Requirements

- Node.js ≥ 18
- Docker (PostgreSQL 16)
- npm

## Setup

### 1. Start PostgreSQL

```bash
docker run -d \
  --name postgres_db \
  -e POSTGRES_USER=admin \
  -e POSTGRES_PASSWORD=admin123 \
  -e POSTGRES_DB=mi_basedatos \
  -p 5432:5432 \
  -v postgres_data:/var/lib/postgresql/data \
  postgres:16
```

### 2. Create schema and GameKey

```bash
# Base schema (if not already created)
docker exec -i postgres_db psql -U admin -d mi_basedatos < ../../DB/db-schema.sql

# Add Kahoot GameKey
docker exec -i postgres_db psql -U admin -d mi_basedatos < ../../DB/init_game_key_kahoot.sql
```

### 3. Environment variables

The `.env.local` file already contains the default configuration:

```env
DATABASE_URL=postgresql://admin:admin123@localhost:5432/mi_basedatos
```

### 4. Install and run

```bash
npm install
PORT=3001 npm start
```

The game will be available at:
- **Landing**: [`http://localhost:3001`](http://localhost:3001) (redirects to English by default)
- **Host/Teacher**: `http://localhost:3001/host_en.html` / `host.html`
- **Students**: `http://localhost:3001/player_en.html` / `player.html`

---

## REST API

| Method | Route                                  | Description                             |
| ------ | -------------------------------------- | --------------------------------------- |
| POST   | `/api/players`                         | Register player (nickname + university) |
| GET    | `/api/leaderboard?game_key=ISO_KAHOOT` | Top scores leaderboard                  |

---

## Game Flow with Persistence

1. **Registration**: When opening `player.html`, a modal asks for nickname and university. It is saved to `localStorage` and the user is created via `/api/players`.
2. **Join**: The player enters the session code. `player.js` enriches the request with `userId` and `university` from `localStorage`.
3. **Start**: When the host clicks "Start match", `persistence-bridge.js` creates a `game_attempt` (status = `STARTED`) for each registered player.
4. **Gameplay**: Each answer is tracked in memory with `questionId`, `choice`, `correct`, `points`, and `timeSeconds`.
5. **End**: When the last question is closed or the host clicks "Finish session", attempts are updated to `COMPLETED` with scores, enriched metadata, and detailed answers.
6. **Disconnect**: If a player disconnects, their attempt is marked as `ABANDONED`.

---

## Data Model (Persistence)

### Tables used

The game uses 3 tables from the shared schema (`db-schema.sql`):

| Table           | Purpose                                |
| --------------- | -------------------------------------- |
| `users`         | Player identity (UUID)                 |
| `game_profiles` | Nickname + university (1:1 with users) |
| `game_attempts` | One record per player per match        |

### `game_attempts` structure

| Column                | Type              | Description                         |
| --------------------- | ----------------- | ----------------------------------- |
| `id`                  | TEXT (UUID)       | Attempt ID                          |
| `user_id`             | TEXT (FK → users) | Player                              |
| `game_key`            | GameKey ENUM      | Always `ISO_KAHOOT`                 |
| `status`              | GameAttemptStatus | `STARTED`, `COMPLETED`, `ABANDONED` |
| `started_at`          | TIMESTAMP         | When the host started the match     |
| `completed_at`        | TIMESTAMP         | When the match ended                |
| `duration_ms`         | INTEGER           | Total duration in ms                |
| `score`               | INTEGER           | Final score                         |
| `max_score`           | INTEGER           | Maximum achievable score            |
| `correct_count`       | INTEGER           | Correct answers                     |
| `incorrect_count`     | INTEGER           | Wrong answers                       |
| `nickname_snapshot`   | TEXT              | Player name at time of play         |
| `university_snapshot` | TEXT              | Player university at time of play   |
| `metadata`            | JSONB             | **Enriched data** (see below)       |

### `metadata` field structure (JSONB)

```jsonc
{
  // ── Session identification ──
  "session_code": "3UMMH",
  "game_id": "iso9241_focus",
  "game_title": "ISO 9241 Usability Sprint",

  // ── Host configuration ──
  "host_config": {
    "title": "ISO Lab class 3B",
    "context": "University e-commerce project",
    "iso_focus": ["ISO 9241", "ISO/IEC 25010:2023"],
    "language": "EN",
    "source": "predefined",
    "timer_seconds": 30
  },

  // ── Player statistics ──
  "total_questions": 4,
  "total_players": 12,
  "final_position": 2,
  "avg_response_time_s": 3.45,
  "fastest_response_s": 1.80,

  // ── Detailed answers (for learning analytics) ──
  "answers": [
    {
      "question_id": "iso9241_q1",
      "question_text": "Which ISO 9241-110 principle is primarily violated?",
      "context": "An HR intranet lists forms in a side menu without icons...",
      "iso_standard": "ISO 9241",
      "difficulty": "easy",
      "options": ["Explicit control", "Self-descriptiveness", "Conformity with expectations", "Error tolerance"],
      "correct_index": 1,
      "player_choice": 1,
      "correct": true,
      "points": 1350,
      "time_seconds": 2.1
    }
  ]
}
```

---

## Useful Queries (PostgreSQL)

### All players from a session

```sql
SELECT
    ga.nickname_snapshot AS player,
    ga.university_snapshot AS university,
    ga.score,
    ga.correct_count,
    ga.incorrect_count,
    ga.status,
    ga.metadata->>'final_position' AS position
FROM game_attempts ga
WHERE ga.game_key = 'ISO_KAHOOT'
  AND ga.metadata->>'session_code' = '3UMMH'
ORDER BY ga.score DESC;
```

### Most failed questions in a session

```sql
SELECT
    answer->>'question_id' AS question,
    answer->>'question_text' AS text,
    answer->>'iso_standard' AS standard,
    answer->>'difficulty' AS difficulty,
    COUNT(*) FILTER (WHERE (answer->>'correct')::boolean = false) AS failures,
    COUNT(*) AS total_answers
FROM game_attempts ga,
     jsonb_array_elements(ga.metadata->'answers') AS answer
WHERE ga.metadata->>'session_code' = '3UMMH'
GROUP BY 1, 2, 3, 4
ORDER BY failures DESC;
```

### Detailed answers from a specific player

```sql
SELECT
    answer->>'question_text' AS question,
    answer->>'correct' AS was_correct,
    answer->>'points' AS points,
    answer->>'time_seconds' AS time_s,
    (answer->>'options')::jsonb->(answer->>'player_choice')::int AS chosen_answer,
    (answer->>'options')::jsonb->(answer->>'correct_index')::int AS correct_answer
FROM game_attempts ga,
     jsonb_array_elements(ga.metadata->'answers') AS answer
WHERE ga.id = '<attempt-uuid>';
```

### Global leaderboard

```sql
SELECT
    ga.nickname_snapshot AS player,
    ga.university_snapshot AS university,
    ga.score,
    ga.correct_count,
    ga.metadata->>'session_code' AS session,
    ga.started_at
FROM game_attempts ga
WHERE ga.game_key = 'ISO_KAHOOT'
  AND ga.status = 'COMPLETED'
ORDER BY ga.score DESC
LIMIT 20;
```
