from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost:5433/postgres"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

def create_tables():
    with engine.begin() as conn:

        # Enable pgvector
        conn.execute(text("""
        CREATE EXTENSION IF NOT EXISTS vector;
        """))

        # PERSONS TABLE
        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS persons (
            person_id UUID PRIMARY KEY,
            full_name TEXT,
            email TEXT,
            phone TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """))

        # FACES TABLE
        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS faces (
            face_id UUID PRIMARY KEY,
            person_id UUID,
            encoding VECTOR(128),
            image_path TEXT,
            confidence DOUBLE PRECISION,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """))

        # FACE SAMPLES TABLE
        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS face_samples (
            sample_id UUID PRIMARY KEY,
            person_id UUID,
            sample_path TEXT,
            sample_vector VECTOR(128),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """))

        # ATTENDANCE TABLE
        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS attendance (
            attendance_id UUID PRIMARY KEY,
            person_id UUID,
            check_in TIMESTAMP,
            check_out TIMESTAMP,
            status TEXT
        );
        """))

        # GEOFENCE TABLE
        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS geofence (
            geofence_id UUID PRIMARY KEY,
            location_name TEXT,
            latitude DOUBLE PRECISION,
            longitude DOUBLE PRECISION,
            radius DOUBLE PRECISION
        );
        """))

        # LOGS TABLE
        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS logs (
            log_id UUID PRIMARY KEY,
            person_id UUID,
            action TEXT,
            log_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """))

    print("All tables created successfully")


print("db.py loaded successfully")
