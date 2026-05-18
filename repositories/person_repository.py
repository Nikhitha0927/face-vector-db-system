from sqlalchemy import text
from db import engine


class PersonRepository:

    def create_person(self, data):

        with engine.begin() as conn:

            conn.execute(text("""
            INSERT INTO persons (
                person_id,
                employee_code,
                full_name,
                email,
                phone,
                department,
                role,
                password_hash
            )
            VALUES (
                gen_random_uuid(),
                :employee_code,
                :full_name,
                :email,
                :phone,
                :department,
                :role,
                :password_hash
            )
            """), data)

    def get_persons(self):

        with engine.begin() as conn:

            result = conn.execute(text("""
            SELECT *
            FROM persons
            WHERE deleted = FALSE
            """))

            return result.fetchall()