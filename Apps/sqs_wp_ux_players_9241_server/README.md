# ISO 9241 Usability Quest — Persistence Server

A gamified workshop where students act as UX auditors, identifying usability violations and proposing solutions based on **ISO 9241** standards. This version adds a **Node.js/Express server** with **PostgreSQL persistence** to track student progress, scores, and detailed answers.

## 🎮 Game Overview

The workshop is structured into three distinct **Labs**, following the ISO 9241 lifecycle:

| Lab       | Focus                | ISO Standard     | Activity                                               |
| :-------- | :------------------- | :--------------- | :----------------------------------------------------- |
| **Lab A** | Discovery & Analysis | ISO 9241-110     | Heuristic evaluation of a B2B dashboard.               |
| **Lab B** | Interaction Redesign | ISO 9241-112/143 | Storyboarding a new flow with better feedback/control. |
| **Lab C** | Validation & Metrics | ISO 9241-210/11  | Defining acceptance criteria and validation plans.     |

### Navigation Modes
- **Full Run:** Navigate typically from Lab A → B → C.
- **Specific Lab (Scoped):** Jump directly to a specific Lab (e.g., Lab B). The game will end automatically after completing that Lab's challenges.

---

## 🛠️ Tech Stack

- **Frontend:** Vanilla JS (ES Modules), no build step required.
- **Backend:** Node.js + Express.
- **Database:** PostgreSQL (using `pg` driver).
- **Persistence:** JSONB column (`metadata`) stores the full rich telemetry of every attempt.

---

## 🚀 Setup & Running

1. **Install Dependencies:**
   ```bash
   npm install
   ```
2. **Database Setup:**
   Ensure your PostgreSQL container is running and register the GameKey:
   ```powershell
   # PowerShell example
   Get-Content "init_game_key.sql" | docker exec -i postgres_db psql -U admin -d mi_basedatos
   ```
3. **Start Server:**
   ```bash
   npm start
   ```
   Server listens on `http://localhost:3002`.

---

## 💾 Data Model

The application uses two main tables in PostgreSQL: `players` and `game_attempts`.

### `players` Table
Stores student identity.
- `id`: UUID
- `nickname`: String (e.g., "Student1")
- `university`: String (e.g., "UFV Madrid")

### `game_attempts` Table
Tracks every session.
- `game_key`: `'ISO_9241_QUEST'`
- `status`: `'STARTED'` | `'COMPLETED'`
- `score`: Integer (0-100)
- `metadata`: **JSONB** containing rich analytics.

### Metadata Structure
The `metadata` JSONB column contains specific details about the run:

```json
{
  "scenario_id": "iso-9241-usability-quest",
  "content_source": "json",
  "target_lab_id": "lab-b",           // null for Full Run, or "lab-x" for Scoped Run
  "completion_mode": "SPECIFIC_LAB",  // "FULL_RUN" or "SPECIFIC_LAB"
  "total_quizzes": 10,
  "score_percentage": 100,
  "labs": [
    { "lab_id": "lab-b", "score": 100, "correct": 2, "total": 2 }
  ],
  "answers": [
    {
      "challenge_id": "challenge-3",
      "lab_id": "lab-b",
      "quiz_id": "c3-q1",
      "question": "Which interaction principle...",
      "player_choice": 1,
      "correct": true,
      "rationale": "..."
    }
  ]
}
```

---

## 📊 Analytics Queries

Use these SQL queries to extract insights from the `game_attempts` table.

### 1. Leaderboard (Who finished with high scores?)
```sql
SELECT 
    p.nickname,
    p.university,
    ga.score,
    (ga.metadata->>'completion_mode') as mode,
    ga.submitted_at
FROM game_attempts ga
JOIN players p ON ga.player_id = p.id
WHERE ga.game_key = 'ISO_9241_QUEST' 
  AND ga.status = 'COMPLETED'
ORDER BY ga.score DESC
LIMIT 20;
```

### 2. Completion Mode Breakdown (Full vs. Lab-only)
```sql
SELECT 
    ga.metadata->>'completion_mode' as mode,
    ga.metadata->>'target_lab_id' as target_lab,
    COUNT(*) as total_attempts,
    AVG(ga.score)::NUMERIC(5,2) as avg_score
FROM game_attempts ga
WHERE ga.game_key = 'ISO_9241_QUEST'
GROUP BY 1, 2;
```

### 3. Quiz Success Rate (Which questions are hardest?)
```sql
SELECT 
    answer->>'lab_id' as lab,
    answer->>'quiz_id' as quiz_id,
    answer->>'question' as question_text,
    COUNT(*) as total_responses,
    SUM(CASE WHEN (answer->>'correct')::boolean THEN 1 ELSE 0 END) as correct_count,
    ROUND((SUM(CASE WHEN (answer->>'correct')::boolean THEN 1 ELSE 0 END)::decimal / COUNT(*)) * 100, 1) as success_rate_pct
FROM game_attempts ga,
     jsonb_array_elements(ga.metadata->'answers') as answer
WHERE ga.game_key = 'ISO_9241_QUEST'
GROUP BY 1, 2, 3
ORDER BY lab, quiz_id;
```

### 4. Player Choice Distribution (What distractors are chosen?)
```sql
SELECT 
    answer->>'quiz_id' as quiz_id,
    answer->>'player_choice' as choice_index,
    COUNT(*) as count
FROM game_attempts ga,
     jsonb_array_elements(ga.metadata->'answers') as answer
WHERE ga.game_key = 'ISO_9241_QUEST'
  AND (answer->>'quiz_id') = 'c1-q1' -- Filter by specific quiz ID
GROUP BY 1, 2
ORDER BY 1, 2;
```
