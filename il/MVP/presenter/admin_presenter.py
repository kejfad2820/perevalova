import sys

sys.path.insert(1, 'il/MVP/')

from model.admin_crud import AdminCRUD

class AdminPRESENTER:
    def __init__(self):
        self.admin_crud = AdminCRUD()

    def get_students(self):
        return self.admin_crud.get_student()

    def get_users(self):
        return self.admin_crud.get_user()

    def get_teachers(self):
        return self.admin_crud.get_teachers()

    def get_enrollments(self):
        return self.admin_crud.get_enrollments()

    def get_courses(self):
        return self.admin_crud.get_courses()