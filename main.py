from db import create_tables
from services.person_service import PersonService


def main():

    try:

        print("Creating database tables...")
        create_tables()

        service = PersonService()

        # CREATE
        person_data = {
    "employee_code": "EMP102",
    "full_name": "Nikhitha",
    "email": "nikhitha102@gmail.com",
    "department": "AI",
    "role": "employee",
    "password_hash": "hashed_password"
}

        person_id = service.register_person(person_data)

        print("Person Created:", person_id)

        # READ
        person = service.fetch_person(person_id)

        print("Fetched Person:")
        print(person)

        # UPDATE
        updated_data = {
            "full_name": "K Nikhitha",
            "department": "AI Research"
        }

        service.edit_person(person_id, updated_data)

        print("Person Updated")

        # DELETE (SOFT DELETE)
        service.remove_person(person_id)

        print("Person Soft Deleted")

    except Exception as e:

        print("Error:", e)


if __name__ == "__main__":
    main()