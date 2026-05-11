from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost:5433/postgres"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)


def create_tables():
    with engine.begin() as conn:

        # Enable extensions
        conn.execute(text("""
        CREATE EXTENSION IF NOT EXISTS vector;
        """))

        conn.execute(text("""
        CREATE EXTENSION IF NOT EXISTS pgcrypto;
        """))

        # 1. ADMIN USERS TABLE
        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS admin_users (
            admin_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            role TEXT CHECK (role IN ('admin','super_admin')),
            email TEXT UNIQUE NOT NULL,
            is_active BOOLEAN DEFAULT TRUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """))

        # 2. GEOFENCE TABLE
        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS geofence (
            geofence_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            location_name TEXT NOT NULL,
            latitude DOUBLE PRECISION,
            longitude DOUBLE PRECISION,
            radius DOUBLE PRECISION,

            created_by UUID REFERENCES admin_users(admin_id),

            is_active BOOLEAN DEFAULT TRUE,
            zone_type TEXT,
            allowed_start_time TIME,
            allowed_end_time TIME,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """))

        # 3. PERSONS TABLE
        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS persons (
            person_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

            employee_code TEXT UNIQUE NOT NULL,
            full_name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT,

            department TEXT,

            role TEXT CHECK (role IN ('employee','manager','admin')),

            password_hash TEXT NOT NULL,

            is_active BOOLEAN DEFAULT TRUE,
            deleted BOOLEAN DEFAULT FALSE,
            deleted_at TIMESTAMP,

            profile_photo TEXT,

            registered_by UUID REFERENCES admin_users(admin_id),

            last_login TIMESTAMP,

            timezone TEXT,

            default_geofence_id UUID REFERENCES geofence(geofence_id),

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """))

        # 4. FACES TABLE
        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS faces (
            face_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

            person_id UUID REFERENCES persons(person_id) ON DELETE CASCADE,

            encoding VECTOR(128),

            image_path TEXT,

            confidence DOUBLE PRECISION,

            angle TEXT,

            blur_score DOUBLE PRECISION,

            quality_score DOUBLE PRECISION,

            liveness_passed BOOLEAN,

            face_width INT,

            face_height INT,

            eye_ratio DOUBLE PRECISION,

            match_threshold DOUBLE PRECISION,

            is_primary BOOLEAN DEFAULT FALSE,

            capture_device TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """))

        # 5. FACE SAMPLES TABLE
        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS face_samples (
            sample_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

            person_id UUID REFERENCES persons(person_id) ON DELETE CASCADE,

            sample_path TEXT,

            sample_vector VECTOR(128),

            angle_type TEXT,

            quality_score DOUBLE PRECISION,

            blur_score DOUBLE PRECISION,

            liveness_passed BOOLEAN,

            capture_order INT,

            approved BOOLEAN,

            rejected_reason TEXT,

            device_info TEXT,

            uploaded_at TIMESTAMP,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """))

        # 6. ATTENDANCE TABLE
        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS attendance (
            attendance_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

            person_id UUID REFERENCES persons(person_id) ON DELETE CASCADE,

            check_in TIMESTAMP,

            check_out TIMESTAMP,

            status TEXT CHECK (status IN ('present','absent','late')),

            latitude DOUBLE PRECISION,

            longitude DOUBLE PRECISION,

            geofence_id UUID REFERENCES geofence(geofence_id),

            inside_geofence BOOLEAN,

            suspicious_flag BOOLEAN,

            confidence_score DOUBLE PRECISION,

            device_id TEXT,

            sync_status TEXT,

            synced_at TIMESTAMP,

            image_path TEXT,

            attendance_type TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """))

        # 7. LOGS TABLE
        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS logs (
            log_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

            person_id UUID REFERENCES persons(person_id) ON DELETE CASCADE,

            action TEXT,

            log_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            table_name TEXT,

            record_id UUID,

            action_by UUID REFERENCES admin_users(admin_id),

            old_data JSONB,

            new_data JSONB,

            ip_address TEXT,

            severity TEXT,

            module_name TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """))

        # 8. REGISTRATION SESSIONS TABLE
        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS registration_sessions (
            session_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

            person_id UUID REFERENCES persons(person_id) ON DELETE CASCADE,

            current_step INT,

            completed_angles TEXT,

            status TEXT,

            started_at TIMESTAMP,

            expires_at TIMESTAMP
        );
        """))

        # INDEXES
        conn.execute(text("""
        CREATE INDEX IF NOT EXISTS idx_faces_person_id
        ON faces(person_id);

        CREATE INDEX IF NOT EXISTS idx_attendance_person_id
        ON attendance(person_id);

        CREATE INDEX IF NOT EXISTS idx_face_samples_person_id
        ON face_samples(person_id);

        CREATE INDEX IF NOT EXISTS idx_logs_person_id
        ON logs(person_id);
        """))

        # PGVECTOR INDEXES
        conn.execute(text("""
        CREATE INDEX IF NOT EXISTS idx_faces_vector
        ON faces
        USING ivfflat (encoding vector_cosine_ops);

        CREATE INDEX IF NOT EXISTS idx_samples_vector
        ON face_samples
        USING ivfflat (sample_vector vector_cosine_ops);
        """))

        # BUSINESS RULE
        conn.execute(text("""
        CREATE UNIQUE INDEX IF NOT EXISTS one_primary_face_per_person
        ON faces(person_id)
        WHERE is_primary = TRUE;
        """))

    print("All tables created successfully")


print("db.py loaded successfully")