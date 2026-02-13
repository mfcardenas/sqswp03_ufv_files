# ISOmillonario — Persistence Server

> 🇪🇸 [Leer en español](./README.md)

Next.js server (TypeScript) that persists every session of the game **"Who wants to be ISOmillionaire"** in PostgreSQL without modifying the original game.

## Architecture

```
public/game/          → Game copy + persistence.js (observes the DOM)
src/app/api/players/  → Player registration
src/app/api/sessions/ → Create/update game sessions
src/app/api/leaderboard/ → Top scores ranking
src/lib/db.ts         → PostgreSQL connection pool
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
# Base schema
docker exec -i postgres_db psql -U admin -d mi_basedatos < ../../DB/db-schema.sql

# Add ISOmillonario GameKey
docker exec -i postgres_db psql -U admin -d mi_basedatos < ../../DB/init_game_key.sql
```

### 3. Environment variables

The `.env.local` file already contains the default configuration:

```env
DATABASE_URL=postgresql://admin:admin123@localhost:5432/mi_basedatos
```

### 4. Install and run

```bash
npm install
npm run dev
```

The game will be available at: [`http://localhost:3000/game/index.html`](http://localhost:3000/game/index.html)

---

## REST API

| Method | Route                                       | Description                             |
| ------ | ------------------------------------------- | --------------------------------------- |
| POST   | `/api/players`                              | Register player (nickname + university) |
| POST   | `/api/sessions`                             | Start game session (STARTED)            |
| PATCH  | `/api/sessions/:id`                         | End session (COMPLETED/ABANDONED)       |
| GET    | `/api/sessions/:id`                         | Get a session                           |
| GET    | `/api/sessions?user_id=X`                   | List sessions for a player              |
| GET    | `/api/leaderboard?game_key=ISO_MILLIONAIRE` | Leaderboard                             |

---

## Game Flow

1. **Registration**: The player enters a nickname and university in a modal when opening the game.
2. **Start**: When clicking "Start", `persistence.js` creates a session (`STARTED`).
3. **Gameplay**: Each answer is logged in memory (correct/incorrect, lifelines used).
4. **End**: On win, loss, or tab close, a `PATCH` is sent with the final result and JSONB metadata.

### Fields stored in `metadata` (JSONB)

```json
{
  "mode": "ai | fallback",
  "language": "ES | EN",
  "total_questions": 15,
  "last_question_level": 12,
  "lifelines_used": { "hint": true, "friend": false, "fifty": true },
  "levels_earned": [1, 2, 3, 4, 5],
  "questions_summary": [
    { "level": 1, "correct": true, "selected_option": 2, "correct_index": 2 }
  ]
}
```

---

## Quick Verification

```bash
# Query saved sessions
docker exec -it postgres_db psql -U admin -d mi_basedatos \
  -c "SELECT id, status, score, correct_count, duration_ms FROM game_attempts WHERE game_key = 'ISO_MILLIONAIRE';"
```

---

## Deploy to Vercel

1. Connect the repository to Vercel.
2. Set the `DATABASE_URL` environment variable with the connection string for your PostgreSQL service (Neon, Supabase, etc.).
3. Deploy — API Routes work as serverless functions automatically.
