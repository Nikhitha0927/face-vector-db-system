from db import engine
from repositories.person_repository import PersonRepository


class PersonService:

    def __init__(self):
        self.repo = PersonRepository()

    def register_person(self, data):

        with engine.begin() as conn:

            person_id = self.repo.create_person(conn, data)

            return person_id

    def fetch_person(self, person_id):

        with engine.begin() as conn:

            return self.repo.get_person(conn, person_id)

    def edit_person(self, person_id, data):

        with engine.begin() as conn:

            self.repo.update_person(conn, person_id, data)

    def remove_person(self, person_id):

        with engine.begin() as conn:

            self.repo.soft_delete_person(conn, person_id)