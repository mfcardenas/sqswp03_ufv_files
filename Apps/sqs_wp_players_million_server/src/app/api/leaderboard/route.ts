import { NextRequest, NextResponse } from "next/server";
import pool from "@/lib/db";

/**
 * GET /api/leaderboard?game_key=ISO_MILLIONAIRE&limit=20
 * Returns top completed attempts, best per user.
 */
export async function GET(request: NextRequest) {
    try {
        const gameKey =
            request.nextUrl.searchParams.get("game_key") ?? "ISO_MILLIONAIRE";
        const limit = Math.min(
            Number(request.nextUrl.searchParams.get("limit") ?? 20),
            100
        );

        const result = await pool.query(
            `SELECT DISTINCT ON (user_id)
         id, user_id, game_key, status, started_at, completed_at,
         duration_ms, score, max_score, correct_count, incorrect_count,
         nickname_snapshot, university_snapshot, metadata
       FROM game_attempts
       WHERE game_key = $1
         AND status = 'COMPLETED'
         AND completed_at IS NOT NULL
       ORDER BY user_id, score DESC, duration_ms ASC, completed_at ASC
       `,
            [gameKey]
        );

        // Sort the distinct-per-user results by ranking criteria
        const ranked = result.rows.sort((a, b) => {
            if (b.score !== a.score) return b.score - a.score;
            if (a.duration_ms !== b.duration_ms)
                return (a.duration_ms ?? Infinity) - (b.duration_ms ?? Infinity);
            return (
                new Date(a.completed_at).getTime() -
                new Date(b.completed_at).getTime()
            );
        });

        return NextResponse.json({ leaderboard: ranked.slice(0, limit) });
    } catch (error: unknown) {
        console.error("GET /api/leaderboard error:", error);
        const message =
            error instanceof Error ? error.message : "Internal server error";
        return NextResponse.json({ error: message }, { status: 500 });
    }
}
