import { NextRequest, NextResponse } from "next/server";
import pool from "@/lib/db";

interface RouteContext {
    params: Promise<{ id: string }>;
}

/**
 * GET /api/sessions/:id
 * Returns a single session by ID.
 */
export async function GET(
    _request: NextRequest,
    context: RouteContext
) {
    try {
        const { id } = await context.params;

        const result = await pool.query(
            `SELECT * FROM game_attempts WHERE id = $1`,
            [id]
        );

        if (result.rows.length === 0) {
            return NextResponse.json({ error: "Session not found" }, { status: 404 });
        }

        return NextResponse.json({ session: result.rows[0] });
    } catch (error: unknown) {
        console.error("GET /api/sessions/:id error:", error);
        const message =
            error instanceof Error ? error.message : "Internal server error";
        return NextResponse.json({ error: message }, { status: 500 });
    }
}

/**
 * PATCH /api/sessions/:id
 * Body: { status, score, correct_count, incorrect_count, duration_ms, metadata }
 * Updates a session (COMPLETED or ABANDONED).
 */
export async function PATCH(
    request: NextRequest,
    context: RouteContext
) {
    try {
        const { id } = await context.params;
        const body = await request.json();
        const {
            status,
            score,
            correct_count,
            incorrect_count,
            duration_ms,
            metadata,
        } = body;

        const now = new Date();
        const completedAt =
            status === "COMPLETED" || status === "ABANDONED" ? now : null;

        const result = await pool.query(
            `UPDATE game_attempts
       SET status = COALESCE($2, status),
           score = COALESCE($3, score),
           correct_count = COALESCE($4, correct_count),
           incorrect_count = COALESCE($5, incorrect_count),
           duration_ms = COALESCE($6, duration_ms),
           completed_at = COALESCE($7, completed_at),
           metadata = COALESCE($8, metadata),
           updated_at = $9
       WHERE id = $1
       RETURNING *`,
            [
                id,
                status ?? null,
                score ?? null,
                correct_count ?? null,
                incorrect_count ?? null,
                duration_ms ?? null,
                completedAt,
                metadata ? JSON.stringify(metadata) : null,
                now,
            ]
        );

        if (result.rows.length === 0) {
            return NextResponse.json({ error: "Session not found" }, { status: 404 });
        }

        return NextResponse.json({ session: result.rows[0] });
    } catch (error: unknown) {
        console.error("PATCH /api/sessions/:id error:", error);
        const message =
            error instanceof Error ? error.message : "Internal server error";
        return NextResponse.json({ error: message }, { status: 500 });
    }
}
