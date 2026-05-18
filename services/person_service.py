from repositories.person_repository import PersonRepository


class PersonService:

    def __init__(self):

        self.repo = PersonRepository()

    def create(self, data):

        self.repo.create_person(data)

    def get_all(self):

        return self.repo.get_persons()