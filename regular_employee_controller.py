import os

from regular_employee_view import RegularEmployeeView
from student_container import StudentContainer
from student_dao import StudentDao


class RegularEmployeeController():

    def __init__(self):
        self.view = RegularEmployeeView()
        self.student_dao = StudentDao()

    def get_student_container(self):
        try:
            return self.student_container
        except AttributeError:
            self.student_container = StudentContainer()
            students = self.student_dao.import_students()
            self.student_container.set_students(students)
        return self.student_container

    def list_students(self):
        students = self.get_student_container().get_all_students()
        students.sort(key=lambda student: student.get_class_name())

        students_data_collection = []
        for count, student in enumerate(students, 1):
                student_data = [count, student.get_name(), student.get_surname(),
                                student.get_email(), student.get_phone_number(), student.get_class_name()]
                students_data_collection.append(student_data)

        self.view.display_list(students_data_collection)

    def run(self):
        self.view.display_welcome_message()

        menu_option = None
        while menu_option != '0':
            os.system('clear')
            self.view.display_employees_menu()
            menu_option = self.view.get_menu_option()

            if menu_option == '1':
                os.system('clear')
                self.list_students()
                self.view.display_continue_key()

        self.view.display_goodbye_message()
