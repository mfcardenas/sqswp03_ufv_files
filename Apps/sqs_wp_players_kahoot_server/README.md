# ISO Kahoot Live Quiz — Servidor de Persistencia

> 🇬🇧 [Read in English](./README_EN.md)

Servidor Express + Socket.IO con persistencia PostgreSQL que registra cada intento de cada jugador en la base de datos, incluyendo las respuestas completas de cada pregunta para análisis de aprendizaje.

## Arquitectura

```
server.js               → Express + Socket.IO (lógica del juego + persistencia)
persistence-bridge.js   → Funciones directas → INSERT/UPDATE game_attempts
persistence.js          → Modal de registro (cliente, player.html)
db.js                   → Pool de conexión PostgreSQL
config.js               → Configuración (LLM, timers, password)
games.js                → Juegos predefinidos (5 sets × 6 preguntas)
styles.css              → Estilos compartidos
```

---

## Requisitos

- Node.js ≥ 18
- Docker (PostgreSQL 16)
- npm

## Configuración

### 1. Levantar PostgreSQL

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

### 2. Crear esquema y GameKey

```bash
# Esquema base (si aún no existe)
docker exec -i postgres_db psql -U admin -d mi_basedatos < ../../DB/db-schema.sql

# Añadir GameKey para Kahoot
docker exec -i postgres_db psql -U admin -d mi_basedatos < ../../DB/init_game_key_kahoot.sql
```

### 3. Variables de entorno

El fichero `.env.local` ya contiene la configuración por defecto:

```env
DATABASE_URL=postgresql://admin:admin123@localhost:5432/mi_basedatos
```

### 4. Instalar y ejecutar

```bash
npm install
PORT=3001 npm start
```

El juego estará disponible en:
- **Landing**: [`http://localhost:3001`](http://localhost:3001) (redirige a inglés por defecto)
- **Docente**: `http://localhost:3001/host_en.html` / `host.html`
- **Estudiantes**: `http://localhost:3001/player_en.html` / `player.html`

---

## API REST

| Método | Ruta                                   | Descripción                                |
| ------ | -------------------------------------- | ------------------------------------------ |
| POST   | `/api/players`                         | Registrar jugador (nickname + universidad) |
| GET    | `/api/leaderboard?game_key=ISO_KAHOOT` | Ranking de mejores intentos                |

---

## Flujo del juego con persistencia

1. **Registro**: Al abrir `player.html`, aparece un modal pidiendo nickname y universidad. Se guarda en `localStorage` y se crea el usuario vía `/api/players`.
2. **Unirse**: El jugador introduce el código de sesión. `player.js` enriquece la solicitud con `userId` y `university` desde `localStorage`.
3. **Inicio**: Cuando el host pulsa "Iniciar partida", `persistence-bridge.js` crea un `game_attempt` (status = `STARTED`) por cada jugador registrado.
4. **Partida**: Cada respuesta se registra en memoria con `questionId`, `choice`, `correct`, `points` y `timeSeconds`.
5. **Fin**: Al cerrar la última pregunta o pulsar "Finalizar sesión", los intentos se actualizan a `COMPLETED` con scores, metadata enriquecida y respuestas detalladas.
6. **Desconexión**: Si un jugador se desconecta, su intento se marca como `ABANDONED`.

---

## Modelo de datos (persistencia)

### Tablas utilizadas

El juego usa 3 tablas del esquema compartido (`db-schema.sql`):

| Tabla           | Propósito                              |
| --------------- | -------------------------------------- |
| `users`         | Identidad del jugador (UUID)           |
| `game_profiles` | Nickname + universidad (1:1 con users) |
| `game_attempts` | Un registro por jugador por partida    |

### Estructura de `game_attempts`

| Columna               | Tipo              | Descripción                         |
| --------------------- | ----------------- | ----------------------------------- |
| `id`                  | TEXT (UUID)       | ID del intento                      |
| `user_id`             | TEXT (FK → users) | Jugador                             |
| `game_key`            | GameKey ENUM      | Siempre `ISO_KAHOOT`                |
| `status`              | GameAttemptStatus | `STARTED`, `COMPLETED`, `ABANDONED` |
| `started_at`          | TIMESTAMP         | Cuando el host inició la partida    |
| `completed_at`        | TIMESTAMP         | Cuando terminó la partida           |
| `duration_ms`         | INTEGER           | Duración total en ms                |
| `score`               | INTEGER           | Puntuación final                    |
| `max_score`           | INTEGER           | Puntuación máxima posible           |
| `correct_count`       | INTEGER           | Aciertos                            |
| `incorrect_count`     | INTEGER           | Errores                             |
| `nickname_snapshot`   | TEXT              | Nombre del jugador al momento       |
| `university_snapshot` | TEXT              | Universidad del jugador al momento  |
| `metadata`            | JSONB             | **Datos enriquecidos** (ver abajo)  |

### Estructura del campo `metadata` (JSONB)

```jsonc
{
  // ── Identificación de sesión ──
  "session_code": "3UMMH",
  "game_id": "iso9241_focus",
  "game_title": "ISO 9241 Usability Sprint",

  // ── Configuración del host ──
  "host_config": {
    "title": "Laboratorio ISO clase 3B",
    "context": "Proyecto e-commerce universitario",
    "iso_focus": ["ISO 9241", "ISO/IEC 25010:2023"],
    "language": "EN",
    "source": "predefined",
    "timer_seconds": 30
  },

  // ── Estadísticas del jugador ──
  "total_questions": 4,
  "total_players": 12,
  "final_position": 2,
  "avg_response_time_s": 3.45,
  "fastest_response_s": 1.80,

  // ── Respuestas detalladas (para análisis de aprendizaje) ──
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

## Consultas útiles (PostgreSQL)

### Todos los jugadores de una sesión

```sql
SELECT
    ga.nickname_snapshot AS jugador,
    ga.university_snapshot AS universidad,
    ga.score,
    ga.correct_count AS aciertos,
    ga.incorrect_count AS errores,
    ga.status,
    ga.metadata->>'final_position' AS posicion
FROM game_attempts ga
WHERE ga.game_key = 'ISO_KAHOOT'
  AND ga.metadata->>'session_code' = '3UMMH'
ORDER BY ga.score DESC;
```

### Preguntas más falladas en una sesión

```sql
SELECT
    answer->>'question_id' AS pregunta,
    answer->>'question_text' AS enunciado,
    answer->>'iso_standard' AS norma,
    answer->>'difficulty' AS dificultad,
    COUNT(*) FILTER (WHERE (answer->>'correct')::boolean = false) AS fallos,
    COUNT(*) AS total_respuestas
FROM game_attempts ga,
     jsonb_array_elements(ga.metadata->'answers') AS answer
WHERE ga.metadata->>'session_code' = '3UMMH'
GROUP BY 1, 2, 3, 4
ORDER BY fallos DESC;
```

### Detalle de respuestas de un jugador

```sql
SELECT
    answer->>'question_text' AS pregunta,
    answer->>'correct' AS acerto,
    answer->>'points' AS puntos,
    answer->>'time_seconds' AS tiempo_s,
    (answer->>'options')::jsonb->(answer->>'player_choice')::int AS respuesta_elegida,
    (answer->>'options')::jsonb->(answer->>'correct_index')::int AS respuesta_correcta
FROM game_attempts ga,
     jsonb_array_elements(ga.metadata->'answers') AS answer
WHERE ga.id = '<attempt-uuid>';
```

### Ranking global

```sql
SELECT
    ga.nickname_snapshot AS jugador,
    ga.university_snapshot AS universidad,
    ga.score,
    ga.correct_count,
    ga.metadata->>'session_code' AS sesion,
    ga.started_at
FROM game_attempts ga
WHERE ga.game_key = 'ISO_KAHOOT'
  AND ga.status = 'COMPLETED'
ORDER BY ga.score DESC
LIMIT 20;
```
