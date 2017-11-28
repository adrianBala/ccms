from regular_employee_view import RegularEmployeeView
import os


class RegularEmployeeController():

    def __init__(self):
        self.view = RegularEmployeeView()

    def list_students(self):
        pass

    def run(self):
        self.view.display_welcome_message()

        menu_option = None
        while menu_option != '0':
            self.view.display_employees_menu()
            menu_option = self.view.get_menu_option()

            if menu_option == '1':
                self.list_students()

        self.view.display_goodbye_message()