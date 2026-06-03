from services.person_service import PersonService
import uuid


def test_create_person():

    service = PersonService()

    data = {
        "employee_code": f"TEST_{uuid.uuid4().hex[:8]}",
        "full_name": "Test User",
        "email": f"{uuid.uuid4().hex[:8]}@gmail.com",
        "department": "QA",
        "role": "employee",
        "password_hash": "hashed"
    }

    person_id = service.register_person(data)

    assert person_id is not None