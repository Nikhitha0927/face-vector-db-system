from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql+psycopg2://postgres:password@localhost:5433/face_vector_db"

# create engine
engine = create_engine(DATABASE_URL)

# create session
SessionLocal = sessionmaker(bind=engine)

# base class for models
Base = declarative_base()

print("db.py loaded successfully")