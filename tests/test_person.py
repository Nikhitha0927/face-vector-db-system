from services.person_service import PersonService


def test_get_persons():

    service = PersonService()

    persons = service.get_all()

    assert persons is not None