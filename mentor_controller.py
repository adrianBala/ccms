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
        students = self.get_student_container().get_students()
        students_data_collection = []
        count = 1
        for student_list in students.values():
            for student in student_list:
                student_data = [count, student.name, student.surname, student.email, student.phone_number, student.class_name]
                students_data_collection.append(student_data)
                count += 1
        self.view.display_list(students_data_collection)

    def get_student_container(self):
        try:
            return self.student_container
        except AttributeError:
            self.student_container = StudentContainer()
            students = self.student_dao.import_students()
            self.student_container.set_students(students)
        return self.student_container

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

    def start(self):
        self.view.display_welcome_message()

        end = False
        while not end:
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
            elif menu_option == '0':
                end = True

        self.view.display_goodbye_message()
