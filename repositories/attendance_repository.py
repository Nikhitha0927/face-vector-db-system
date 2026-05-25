from sqlalchemy import text


class AttendanceRepository:

    def create_attendance(
        self,
        conn,
        data
    ):

        query = text("""

            INSERT INTO attendance (
                person_id,
                check_in,
                status
            )

            VALUES (
                :person_id,
                CURRENT_TIMESTAMP,
                :status
            )

            RETURNING attendance_id
        """)

        result = conn.execute(query, data)

        return result.fetchone()[0]

    def get_attendance_by_id(
        self,
        conn,
        attendance_id
    ):

        query = text("""

            SELECT *
            FROM attendance
            WHERE attendance_id = :attendance_id
        """)

        result = conn.execute(query, {
            "attendance_id": attendance_id
        })

        return result.fetchone()

    def update_attendance(
        self,
        conn,
        attendance_id,
        data
    ):

        query = text("""

            UPDATE attendance
            SET status = :status
            WHERE attendance_id = :attendance_id
        """)

        conn.execute(query, {
            "status": data["status"],
            "attendance_id": attendance_id
        })

    def delete_attendance(
        self,
        conn,
        attendance_id
    ):

        query = text("""

            DELETE FROM attendance
            WHERE attendance_id = :attendance_id
        """)

        conn.execute(query, {
            "attendance_id": attendance_id
        })