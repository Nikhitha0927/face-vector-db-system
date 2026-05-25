from sqlalchemy import text


class FaceRepository:

    def create_face(self, conn, data):

        query = text("""

            INSERT INTO faces (
                person_id,
                encoding,
                image_path,
                confidence
            )

            VALUES (
                :person_id,
                :encoding,
                :image_path,
                :confidence
            )

            RETURNING face_id
        """)

        result = conn.execute(query, data)

        return result.fetchone()[0]

    def get_face_by_id(self, conn, face_id):

        query = text("""

            SELECT *
            FROM faces
            WHERE face_id = :face_id
        """)

        result = conn.execute(query, {
            "face_id": face_id
        })

        return result.fetchone()

    def update_face(
        self,
        conn,
        face_id,
        data
    ):

        query = text("""

            UPDATE faces
            SET confidence = :confidence
            WHERE face_id = :face_id
        """)

        conn.execute(query, {
            "confidence": data["confidence"],
            "face_id": face_id
        })

    def delete_face(self, conn, face_id):

        query = text("""

            DELETE FROM faces
            WHERE face_id = :face_id
        """)

        conn.execute(query, {
            "face_id": face_id
        })