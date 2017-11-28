from mentor_view import MentorView
from student_dao import StudentDao
from student_container import StudentContainer
import os


class MentorController():

    def __init__(self, user_base_dao, user_base_container):
        self.view = MentorView()
        self.student_dao = StudentDao()
        self.user_base_dao = user_base_dao
        self.user_base_container = user_base_container

    def list_students(self):
        pass

    def get_student_container(self):
        try:
            return self.student_container
        except AttributeError:
            self.student_container = StudentContainer()
            students = self.student_dao.import_students()
            self.student_container.set_students(students)
        return self.student_container

    def add_student(self):
        students_data = self.view.get_students_data_from_user()
        students_name, students_surname, students_email, students_phone, students_password, students_class = students_data

        student = self.student_dao.create_student(*students_data)
        self.get_student_container().add_student(student, students_class)
        students = self.get_student_container().get_students()
        self.student_dao.export_students(students)

        self.user_base_container.add_user(students_email, students_password, 'student')
        login_info = self.user_base_container.get_login_info()
        self.user_base_dao.export_login_info(login_info)

        self.view.display_message("Student added!")

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
