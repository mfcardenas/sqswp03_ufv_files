import { NextRequest, NextResponse } from "next/server";
import pool from "@/lib/db";
import { v4 as uuidv4 } from "uuid";

/**
 * POST /api/players
 * Body: { nickname: string, university: string }
 * Creates user + game_profiles if not exists, returns { user_id, profile_id }.
 */
export async function POST(request: NextRequest) {
    try {
        const body = await request.json();
        const { nickname, university } = body;

        if (!nickname || !university) {
            return NextResponse.json(
                { error: "nickname and university are required" },
                { status: 400 }
            );
        }

        // Check if profile already exists by nickname
        const existing = await pool.query(
            `SELECT gp.id AS profile_id, gp.user_id
       FROM game_profiles gp
       WHERE LOWER(gp.nickname) = LOWER($1)`,
            [nickname]
        );

        if (existing.rows.length > 0) {
            return NextResponse.json({
                user_id: existing.rows[0].user_id,
                profile_id: existing.rows[0].profile_id,
                existing: true,
            });
        }

        // Create new user + profile in a transaction
        const client = await pool.connect();
        try {
            await client.query("BEGIN");

            const userId = uuidv4();
            const profileId = uuidv4();
            const now = new Date();

            await client.query(
                `INSERT INTO users (id, created_at, updated_at) VALUES ($1, $2, $3)`,
                [userId, now, now]
            );

            await client.query(
                `INSERT INTO game_profiles (id, user_id, nickname, university, created_at, updated_at)
         VALUES ($1, $2, $3, $4, $5, $6)`,
                [profileId, userId, nickname, university, now, now]
            );

            await client.query("COMMIT");

            return NextResponse.json(
                { user_id: userId, profile_id: profileId, existing: false },
                { status: 201 }
            );
        } catch (err) {
            await client.query("ROLLBACK");
            throw err;
        } finally {
            client.release();
        }
    } catch (error: unknown) {
        console.error("POST /api/players error:", error);
        const message = error instanceof Error ? error.message : "Internal server error";
        return NextResponse.json({ error: message }, { status: 500 });
    }
}
