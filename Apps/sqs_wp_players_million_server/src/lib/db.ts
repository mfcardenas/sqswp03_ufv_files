import { Pool } from "pg";

const pool = new Pool({
  connectionString:
    process.env.DATABASE_URL ??
    "postgresql://admin:admin123@localhost:5432/mi_basedatos",
});

export default pool;
