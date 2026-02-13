-- ============================================
-- CORE GAME SCHEMA (excludes quiz-specific tables)
-- ============================================
-- Existing keys in this project:
-- QUIZ_12207, ROLLERCOASTER_29110
-- To add a new game, add a new enum value below.
CREATE TYPE "GameKey" AS ENUM ('QUIZ_12207', 'ROLLERCOASTER_29110');
CREATE TYPE "GameAttemptStatus" AS ENUM ('STARTED', 'COMPLETED', 'ABANDONED');
-- Auth user table (already exists in the system)
CREATE TABLE users (
  id         TEXT PRIMARY KEY,
  created_at TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP(3) NOT NULL
);
-- 1 user = 1 game profile (global nickname/university)
CREATE TABLE game_profiles (
  id         TEXT PRIMARY KEY,
  user_id    TEXT NOT NULL REFERENCES users(id) ON UPDATE CASCADE ON DELETE CASCADE,
  nickname   TEXT NOT NULL,
  university TEXT NOT NULL,
  created_at TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP(3) NOT NULL
);
CREATE UNIQUE INDEX game_profiles_user_id_key ON game_profiles(user_id);
CREATE UNIQUE INDEX game_profiles_nickname_key ON game_profiles(nickname);
CREATE INDEX game_profiles_nickname_idx ON game_profiles(nickname);
-- One attempt row per game session
CREATE TABLE game_attempts (
  id                  TEXT PRIMARY KEY,
  user_id             TEXT NOT NULL REFERENCES users(id) ON UPDATE CASCADE ON DELETE CASCADE,
  game_key            "GameKey" NOT NULL,
  status              "GameAttemptStatus" NOT NULL DEFAULT 'STARTED',
  started_at          TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
  completed_at        TIMESTAMP(3),
  duration_ms         INTEGER,
  score               INTEGER NOT NULL DEFAULT 0,
  max_score           INTEGER NOT NULL DEFAULT 0,
  correct_count       INTEGER NOT NULL DEFAULT 0,
  incorrect_count     INTEGER NOT NULL DEFAULT 0,
  nickname_snapshot   TEXT NOT NULL,
  university_snapshot TEXT NOT NULL,
  metadata            JSONB,
  created_at          TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at          TIMESTAMP(3) NOT NULL
);
CREATE INDEX game_attempts_user_id_game_key_started_at_idx
  ON game_attempts (user_id, game_key, started_at);
CREATE INDEX game_attempts_game_key_status_score_duration_ms_completed_at_idx
  ON game_attempts (game_key, status, score, duration_ms, completed_at);

-- ============================================
-- ADDING A NEW GAME
-- ============================================
-- To add a new game, simply add a new value to the GameKey enum:
-- ALTER TYPE "GameKey" ADD VALUE 'ISO_MILLIONAIRE';
-- ALTER TYPE "GameKey" ADD VALUE 'ISO_29148_REQUIREMENTS';
-- ALTER TYPE "GameKey" ADD VALUE 'ISO_QUIZ_CLOUD';
