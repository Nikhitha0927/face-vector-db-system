from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost:5433/postgres"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)


def create_tables():
    with engine.begin() as conn:

        # Enable pgvector extension
        conn.execute(text("""
        CREATE EXTENSION IF NOT EXISTS vector;
        """))

        # 1. GEOFENCE TABLE
        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS geofence (
            geofence_id UUID PRIMARY KEY,
            location_name TEXT,
            latitude DOUBLE PRECISION,
            longitude DOUBLE PRECISION,
            radius DOUBLE PRECISION,

            created_by UUID,
            is_active BOOLEAN DEFAULT TRUE,
            zone_type TEXT,
            allowed_start_time TIME,
            allowed_end_time TIME,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP
        );
        """))

        # 2. PERSONS TABLE
        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS persons (
            person_id UUID PRIMARY KEY,
            employee_code TEXT,
            full_name TEXT,
            email TEXT,
            phone TEXT,
            department TEXT,
            role TEXT,
            password_hash TEXT,
            is_active BOOLEAN DEFAULT TRUE,
            deleted BOOLEAN DEFAULT FALSE,
            deleted_at TIMESTAMP,
            profile_photo TEXT,
            registered_by UUID,
            last_login TIMESTAMP,
            timezone TEXT,

            default_geofence_id UUID REFERENCES geofence(geofence_id),

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP
        );
        """))

        # 3. FACES TABLE
        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS faces (
            face_id UUID PRIMARY KEY,

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
            is_primary BOOLEAN,
            capture_device TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP
        );
        """))

        # 4. FACE SAMPLES TABLE
        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS face_samples (
            sample_id UUID PRIMARY KEY,

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

        # 5. ATTENDANCE TABLE
        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS attendance (
            attendance_id UUID PRIMARY KEY,

            person_id UUID REFERENCES persons(person_id) ON DELETE CASCADE,

            check_in TIMESTAMP,
            check_out TIMESTAMP,
            status TEXT,

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
            updated_at TIMESTAMP
        );
        """))

        # 6. LOGS TABLE
        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS logs (
            log_id UUID PRIMARY KEY,

            person_id UUID REFERENCES persons(person_id) ON DELETE CASCADE,

            action TEXT,
            log_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            table_name TEXT,
            record_id UUID,
            action_by UUID,
            old_data JSONB,
            new_data JSONB,
            ip_address TEXT,
            severity TEXT,
            module_name TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """))

        # 7. ADMIN USERS TABLE
        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS admin_users (
            admin_id UUID PRIMARY KEY,

            username TEXT,
            password_hash TEXT,
            role TEXT,
            email TEXT,

            is_active BOOLEAN DEFAULT TRUE,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """))

        # 8. REGISTRATION SESSIONS TABLE
        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS registration_sessions (
            session_id UUID PRIMARY KEY,

            person_id UUID REFERENCES persons(person_id) ON DELETE CASCADE,

            current_step INT,
            completed_angles TEXT,
            status TEXT,
            started_at TIMESTAMP,
            expires_at TIMESTAMP
        );
        """))

    print("All tables created successfully")


print("db.py loaded successfully")