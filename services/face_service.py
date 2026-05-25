from repositories.face_repository import FaceRepository
from db import engine


class FaceService:

    def __init__(self):
        self.repo = FaceRepository()

    def add_face(self, data):

        with engine.begin() as conn:
            face_id = self.repo.create_face(conn, data)
            return face_id

    def get_face(self, face_id):

        with engine.begin() as conn:
            return self.repo.get_face_by_id(conn, face_id)

    def update_face(self, face_id, data):

        with engine.begin() as conn:
            self.repo.update_face(conn, face_id, data)

    def delete_face(self, face_id):

        with engine.begin() as conn:
            self.repo.delete_face(conn, face_id)