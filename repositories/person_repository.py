from sqlalchemy import text
from services.audit_service import log_action


class PersonRepository:

    def create_person(self, conn, data):

        query = text("""
            INSERT INTO persons (
                employee_code,
                full_name,
                email,
                department,
                role,
                password_hash,
                created_at,
                updated_at
            )
            VALUES (
                :employee_code,
                :full_name,
                :email,
                :department,
                :role,
                :password_hash,
                CURRENT_TIMESTAMP,
                CURRENT_TIMESTAMP
            )
            RETURNING person_id
        """)

        result = conn.execute(query, data)

        person_id = result.fetchone()[0]

        log_action(
            conn=conn,
            person_id=person_id,
            action="CREATE",
            table_name="persons",
            record_id=person_id,
            old_data=None,
            new_data=str(data)
        )

        return person_id

    def get_person(self, conn, person_id):

        query = text("""
            SELECT *
            FROM persons
            WHERE person_id = :person_id
            AND deleted = FALSE
        """)

        result = conn.execute(query, {
            "person_id": person_id
        })

        return result.fetchone()

    def update_person(self, conn, person_id, data):

        query = text("""
            UPDATE persons
            SET
                full_name = :full_name,
                department = :department,
                updated_at = CURRENT_TIMESTAMP
            WHERE person_id = :person_id
        """)

        conn.execute(query, {
            "person_id": person_id,
            "full_name": data["full_name"],
            "department": data["department"]
        })

        log_action(
            conn=conn,
            person_id=person_id,
            action="UPDATE",
            table_name="persons",
            record_id=person_id,
            old_data=None,
            new_data=str(data)
        )

    def soft_delete_person(self, conn, person_id):

        query = text("""
            UPDATE persons
            SET
                deleted = TRUE,
                deleted_at = CURRENT_TIMESTAMP
            WHERE person_id = :person_id
        """)

        conn.execute(query, {
            "person_id": person_id
        })

        log_action(
            conn=conn,
            person_id=person_id,
            action="DELETE",
            table_name="persons",
            record_id=person_id,
            old_data=None,
            new_data='{"deleted": true}'
        )