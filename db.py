from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost:5433/postgres"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def create_tables():

    with engine.connect() as conn:

        conn.execute(text("""
        CREATE EXTENSION IF NOT EXISTS vector;
        """))

        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS faces (
            id SERIAL PRIMARY KEY,
            person_id UUID,
            name VARCHAR(255),
            encoding VECTOR(128),
            image_path TEXT,
            confidence FLOAT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """))

        conn.commit()

print("db.py loaded successfully")
