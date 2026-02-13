import { NextRequest, NextResponse } from "next/server";
import pool from "@/lib/db";
import { v4 as uuidv4 } from "uuid";

/**
 * POST /api/sessions
 * Body: { user_id, nickname, university, mode }
 * Creates a new game_attempts row with status='STARTED'.
 */
export async function POST(request: NextRequest) {
    try {
        const body = await request.json();
        const { user_id, nickname, university, mode } = body;

        if (!user_id || !nickname || !university) {
            return NextResponse.json(
                { error: "user_id, nickname, and university are required" },
                { status: 400 }
            );
        }

        const sessionId = uuidv4();
        const now = new Date();

        await pool.query(
            `INSERT INTO game_attempts
        (id, user_id, game_key, status, started_at, score, max_score,
         correct_count, incorrect_count, nickname_snapshot, university_snapshot,
         metadata, created_at, updated_at)
       VALUES ($1, $2, 'ISO_MILLIONAIRE', 'STARTED', $3, 0, 1000000,
               0, 0, $4, $5, $6, $7, $8)`,
            [
                sessionId,
                user_id,
                now,
                nickname,
                university,
                JSON.stringify({ mode: mode || "fallback" }),
                now,
                now,
            ]
        );

        return NextResponse.json({ session_id: sessionId }, { status: 201 });
    } catch (error: unknown) {
        console.error("POST /api/sessions error:", error);
        const message = error instanceof Error ? error.message : "Internal server error";
        return NextResponse.json({ error: message }, { status: 500 });
    }
}

/**
 * GET /api/sessions
 * Query: ?user_id=xxx
 * Returns all sessions for a user.
 */
export async function GET(request: NextRequest) {
    try {
        const userId = request.nextUrl.searchParams.get("user_id");

        if (!userId) {
            return NextResponse.json(
                { error: "user_id query param is required" },
                { status: 400 }
            );
        }

        const result = await pool.query(
            `SELECT * FROM game_attempts
       WHERE user_id = $1 AND game_key = 'ISO_MILLIONAIRE'
       ORDER BY started_at DESC`,
            [userId]
        );

        return NextResponse.json({ sessions: result.rows });
    } catch (error: unknown) {
        console.error("GET /api/sessions error:", error);
        const message = error instanceof Error ? error.message : "Internal server error";
        return NextResponse.json({ error: message }, { status: 500 });
    }
}
