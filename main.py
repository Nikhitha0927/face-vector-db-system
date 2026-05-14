from db import engine
from sqlalchemy import text
import uuid


# =========================
# CREATE PERSON
# =========================
def create_person():

    with engine.begin() as conn:

        # CHECK IF PERSON EXISTS
        existing_person = conn.execute(text("""
        SELECT person_id
        FROM persons
        WHERE employee_code = :employee_code
        """), {
            "employee_code": "EMP001"
        }).fetchone()

        # RETURN EXISTING PERSON
        if existing_person:

            print("Person already exists")

            return str(existing_person[0])

        # CREATE NEW PERSON
        person_id = str(uuid.uuid4())

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
            :person_id,
            :employee_code,
            :full_name,
            :email,
            :phone,
            :department,
            :role,
            :password_hash
        )
        """), {
            "person_id": person_id,
            "employee_code": "EMP001",
            "full_name": "Nikhitha",
            "email": "nikhitha@gmail.com",
            "phone": "9876543210",
            "department": "AI",
            "role": "employee",
            "password_hash": "hashed_password"
        })

    print("Person inserted successfully")

    return person_id


# =========================
# CREATE FACE
# =========================
def create_face(person_id):

    with engine.begin() as conn:

        # CHECK IF FACE EXISTS
        existing_face = conn.execute(text("""
        SELECT face_id
        FROM faces
        WHERE person_id = :person_id
        """), {
            "person_id": person_id
        }).fetchone()

        if existing_face:

            print("Face already exists")

            return

        # 128-D VECTOR
        vector_data = ",".join(["0.1"] * 128)

        conn.execute(text(f"""
        INSERT INTO faces (
            person_id,
            encoding,
            image_path,
            confidence
        )
        VALUES (
            :person_id,
            ARRAY[{vector_data}]::vector,
            :image_path,
            :confidence
        )
        """), {
            "person_id": person_id,
            "image_path": "sample.jpg",
            "confidence": 0.95
        })

    print("Face inserted successfully")


# =========================
# READ PERSONS
# =========================
def get_persons():

    with engine.begin() as conn:

        result = conn.execute(text("""
        SELECT *
        FROM persons
        WHERE is_deleted = FALSE
        """))

        print("\n===== PERSONS =====")

        for row in result:
            print(row)


# =========================
# UPDATE PERSON
# =========================
def update_person():

    with engine.begin() as conn:

        conn.execute(text("""
        UPDATE persons
        SET department = :department
        WHERE employee_code = :employee_code
        """), {
            "department": "Machine Learning",
            "employee_code": "EMP001"
        })

    print("Person updated successfully")


# =========================
# SOFT DELETE PERSON
# =========================
def delete_person():

    with engine.begin() as conn:

        conn.execute(text("""
        UPDATE persons
        SET is_deleted = TRUE,
            deleted_at = CURRENT_TIMESTAMP
        WHERE employee_code = :employee_code
        """), {
            "employee_code": "EMP001"
        })

    print("Person soft deleted successfully")


# =========================
# MAIN
# =========================
if __name__ == "__main__":

    # CREATE PERSON
    person_id = create_person()

    # CREATE FACE
    create_face(person_id)

    # READ
    get_persons()

    # UPDATE
    update_person()

    # READ AGAIN
    get_persons()

    # DELETE
    delete_person()

    # FINAL READ
    get_persons()