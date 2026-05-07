from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

# 🔗 Change this if needed
DATABASE_URL = "postgresql+psycopg2://postgres:password@localhost:5432/face_vector_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

print("db.py loaded successfully")

# ✅ Create table using raw SQL (because VECTOR is extension type)
def create_tables():
    with engine.connect() as conn:
        conn.execute(text("CREATE EXTENSION IF NOT EXISTS vector;"))

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

        print("faces table created successfully")