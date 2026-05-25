from sqlalchemy import text
from db import engine


def test_faces_table_exists():

    with engine.connect() as conn:

        result = conn.execute(text("""
            SELECT EXISTS (
                SELECT FROM information_schema.tables
                WHERE table_name = 'faces'
            );
        """))

        exists = result.scalar()

        assert exists is True