from regular_employee_view import RegularEmployeeView
from student_container import StudentContainer
from student_dao import StudentDao
import os


class RegularEmployeeController():

    def __init__(self):
        self.view = RegularEmployeeView()
        self.student_dao = StudentDao()

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

    def run(self):
        self.view.display_welcome_message()

        menu_option = None
        while menu_option != '0':
            self.view.display_employees_menu()
            menu_option = self.view.get_menu_option()

            if menu_option == '1':
                self.list_students()

        self.view.display_goodbye_message()
