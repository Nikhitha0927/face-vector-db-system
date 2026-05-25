from repositories.attendance_repository import AttendanceRepository
from db import engine


class AttendanceService:

    def __init__(self):
        self.repo = AttendanceRepository()

    def mark_attendance(self, data):

        with engine.begin() as conn:
            attendance_id = self.repo.create_attendance(conn, data)
            return attendance_id

    def get_attendance(self, attendance_id):

        with engine.begin() as conn:
            return self.repo.get_attendance_by_id(
                conn,
                attendance_id
            )

    def update_attendance(
        self,
        attendance_id,
        data
    ):

        with engine.begin() as conn:
            self.repo.update_attendance(
                conn,
                attendance_id,
                data
            )

    def delete_attendance(self, attendance_id):

        with engine.begin() as conn:
            self.repo.delete_attendance(
                conn,
                attendance_id
            )