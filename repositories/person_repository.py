from sqlalchemy import text
from db import engine

def create_person(data):
    with engine.begin() as conn:
        conn.execute(text("""
        INSERT INTO persons(
            employee_code,
            full_name,
            email,
            password_hash
        )
        VALUES(
            :employee_code,
            :full_name,
            :email,
            :password_hash
        )
        """), data)