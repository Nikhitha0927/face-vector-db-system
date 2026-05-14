from alembic import op


# revision identifiers
revision = 'eba64ac00f77'
down_revision = 'ebb0c4f64ecf'
branch_labels = None
depends_on = None


def upgrade():

    # GEOFENCE
    op.execute("""
    CREATE TABLE geofence (
        geofence_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        location_name TEXT,
        latitude DOUBLE PRECISION,
        longitude DOUBLE PRECISION,
        radius DOUBLE PRECISION
    );
    """)

    # FACE SAMPLES
    op.execute("""
    CREATE TABLE face_samples (
        sample_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        person_id UUID REFERENCES persons(person_id) ON DELETE CASCADE,
        sample_vector vector(128),
        sample_path TEXT
    );
    """)

    # LOGS
    op.execute("""
    CREATE TABLE logs (
        log_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        person_id UUID REFERENCES persons(person_id) ON DELETE CASCADE,
        action TEXT,
        created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # ADMIN USERS
    op.execute("""
    CREATE TABLE admin_users (
        admin_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        username TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    );
    """)

    # REGISTRATION SESSIONS
    op.execute("""
    CREATE TABLE registration_sessions (
        session_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        person_id UUID REFERENCES persons(person_id) ON DELETE CASCADE,
        current_step INTEGER,
        status TEXT
    );
    """)


def downgrade():

    op.execute("DROP TABLE IF EXISTS registration_sessions;")
    op.execute("DROP TABLE IF EXISTS admin_users;")
    op.execute("DROP TABLE IF EXISTS logs;")
    op.execute("DROP TABLE IF EXISTS face_samples;")
    op.execute("DROP TABLE IF EXISTS geofence;")
