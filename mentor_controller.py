from mentor_view import MentorView
from student_dao import StudentDao
import os


class MentorController():

    def __init__(self, user_base_dao, user_base_container):
        self.view = MentorView()
        self.student_dao = StudentDao()
        self.user_base_dao = user_base_dao
        self.user_base_container = user_base_container

    def list_students(self):
        pass

    def add_student(self):
        student_data = self.view.get_students_data_from_user()
        student = self.student_dao.create_student(student_data)
        self.student_dao.export_student(student)

    def remove_student(self):
        pass

    def edit_student(self):
        pass

    def add_assignment(self):
        pass

    def grade_assignment(self):
        pass

    def check_attendance(self):
        pass

    def run(self):
        self.view.display_welcome_message()

        menu_option = None
        while menu_option != '0':
            self.view.display_mentors_menu()
            menu_option = self.view.get_menu_option()

            if menu_option == '1':
                self.list_students()
            elif menu_option == '2':
                self.add_student()
            elif menu_option == '3':
                self.remove_student()
            elif menu_option == '4':
                self.edit_student()
            elif menu_option == '5':
                self.add_assignment()
            elif menu_option == '6':
                self.grade_assignment()
            elif menu_option == '7':
                self.check_attendance()

        self.view.display_goodbye_message()