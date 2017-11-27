from regular_employee_view import RegularEmployeeView
import os


class RegularEmployeeController():

    def __init__(self):
        self.view = RegularEmployeeView()

    def list_students(self):
        pass

    def start(self):
        end = False
        while not end:
            self.view.display_employees_menu()
            menu_option = self.view.get_menu_option()

            if menu_option == '1':
                self.list_students()
            elif menu_option == '0':
                end = True
