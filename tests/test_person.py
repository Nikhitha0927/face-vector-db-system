from services.person_service import PersonService


def test_create_person():

    service = PersonService()

    data = {
        "employee_code": "TEST101",
        "full_name": "Test User",
        "email": "testuser@gmail.com",
        "department": "QA",
        "role": "employee",
        "password_hash": "hashed"
    }

    person_id = service.register_person(data)

    assert person_id is not None