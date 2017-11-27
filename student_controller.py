from student_view import StudentView
import os


class StudentController():

    def __init__(self):
        self.view = StudentView()

    def view_grades(self):
        pass

    def submit_assignment(self):
        pass

    def start(self):
        self.view.display_welcome_message()

        end = False
        while not end:
            self.view.display_students_menu()
            menu_option = self.view.get_menu_option()

            if menu_option == '1':
                self.view_grades()
            elif menu_option == '2':
                self.submit_assignment()
            elif menu_option == '0':
                end = True

        self.view.display_goodbye_message()
