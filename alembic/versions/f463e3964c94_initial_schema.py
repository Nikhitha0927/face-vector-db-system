from alembic import op
import sqlalchemy as sa


revision = 'f463e3964c94'
down_revision = None


def upgrade() -> None:

    # =========================
    # EXTENSIONS
    # =========================
    op.execute("CREATE EXTENSION IF NOT EXISTS pgcrypto;")
    op.execute("CREATE EXTENSION IF NOT EXISTS vector;")

    # =========================
    # PERSONS TABLE
    # =========================
    op.execute("""
    CREATE TABLE persons (
        person_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        employee_code TEXT UNIQUE NOT NULL,
        full_name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        phone TEXT,
        department TEXT,
        role TEXT,
        password_hash TEXT NOT NULL,
        is_active BOOLEAN DEFAULT TRUE,
        is_deleted BOOLEAN DEFAULT FALSE,
        deleted_at TIMESTAMP WITH TIME ZONE,
        created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # =========================
    # FACES TABLE (VECTOR)
    # =========================
    op.execute("""
    CREATE TABLE faces (
        face_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        person_id UUID REFERENCES persons(person_id) ON DELETE CASCADE,
        encoding vector(128),
        image_path TEXT,
        confidence FLOAT,
        created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # =========================
    # ATTENDANCE TABLE
    # =========================
    op.execute("""
    CREATE TABLE attendance (
        attendance_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        person_id UUID REFERENCES persons(person_id) ON DELETE CASCADE,
        check_in TIMESTAMP WITH TIME ZONE,
        check_out TIMESTAMP WITH TIME ZONE,
        status TEXT,
        created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
    );
    """)


def downgrade() -> None:
    op.execute("DROP TABLE IF EXISTS attendance;")
    op.execute("DROP TABLE IF EXISTS faces;")
    op.execute("DROP TABLE IF EXISTS persons;")
