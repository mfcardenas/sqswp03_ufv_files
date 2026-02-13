# ISOmillonario — Servidor de Persistencia

> 🇬🇧 [Read in English](./README_EN.md)

Servidor Next.js (TypeScript) que persiste cada sesión del juego **"Quien quiere ser ISOmillonario"** en PostgreSQL sin modificar el juego original.

## Arquitectura

```
public/game/          → Copia del juego + persistence.js (observa el DOM)
src/app/api/players/  → Registro de jugadores
src/app/api/sessions/ → Crear/actualizar sesiones de juego
src/app/api/leaderboard/ → Ranking de mejores intentos
src/lib/db.ts         → Pool de conexión PostgreSQL
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
# Esquema base
docker exec -i postgres_db psql -U admin -d mi_basedatos < ../../DB/db-schema.sql

# Añadir GameKey del juego ISOmillonario
docker exec -i postgres_db psql -U admin -d mi_basedatos < ../../DB/init_game_key.sql
```

### 3. Variables de entorno

El fichero `.env.local` ya contiene la configuración por defecto:

```env
DATABASE_URL=postgresql://admin:admin123@localhost:5432/mi_basedatos
```

### 4. Instalar y ejecutar

```bash
npm install
npm run dev
```

El juego estará disponible en: [`http://localhost:3000/game/index.html`](http://localhost:3000/game/index.html)

---

## API REST

| Método | Ruta                                        | Descripción                            |
| ------ | ------------------------------------------- | -------------------------------------- |
| POST   | `/api/players`                              | Registrar jugador (nickname + uni)     |
| POST   | `/api/sessions`                             | Iniciar sesión de juego (STARTED)      |
| PATCH  | `/api/sessions/:id`                         | Finalizar sesión (COMPLETED/ABANDONED) |
| GET    | `/api/sessions/:id`                         | Consultar una sesión                   |
| GET    | `/api/sessions?user_id=X`                   | Listar sesiones de un jugador          |
| GET    | `/api/leaderboard?game_key=ISO_MILLIONAIRE` | Ranking                                |

---

## Flujo del juego

1. **Registro**: El jugador introduce nickname y universidad en un modal al abrir el juego.
2. **Inicio**: Al pulsar "Empezar", `persistence.js` crea una sesión (`STARTED`).
3. **Partida**: Cada respuesta se registra en memoria (aciertos, fallos, comodines).
4. **Fin**: Al ganar, perder o cerrar la pestaña, se envía `PATCH` con el resultado final y metadata JSONB.

### Campos almacenados en `metadata` (JSONB)

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

## Verificación rápida

```bash
# Consultar sesiones guardadas
docker exec -it postgres_db psql -U admin -d mi_basedatos \
  -c "SELECT id, status, score, correct_count, duration_ms FROM game_attempts WHERE game_key = 'ISO_MILLIONAIRE';"
```

---

## Despliegue en Vercel

1. Conectar el repositorio a Vercel.
2. Configurar la variable de entorno `DATABASE_URL` con la cadena de conexión del servicio PostgreSQL (Neon, Supabase, etc.).
3. Desplegar — los API Routes funcionan como funciones serverless automáticamente.
