import os

from assignment_container import AssignmentContainer
from assignment_dao import AssignmentDao
from student_container import StudentContainer
from student_view import StudentView


class StudentController():

    def __init__(self, email=''):
        self.view = StudentView()
        self.email = email
        self.assignment_dao = AssignmentDao()

    def get_assignment_container(self):
        try:
            return self.assignment_container
        except AttributeError:
            self.assignment_container = AssignmentContainer()
            assignments = self.assignment_dao.import_assignments()
            self.assignment_container.set_assignments(assignments)
        return self.assignment_container

    def list_student_assignments(self):
        assignments_data_collection = []

        student_assignments = self.get_assignment_container().get_assignments_of_student(self.email)
        for count, assignment in enumerate(student_assignments, 1):
            assignment_data = [count, assignment.get_name(), assignment.get_url(),
                               assignment.get_grade()]
            assignments_data_collection.append(assignment_data)

        return assignments_data_collection

    def view_grades(self):
        self.view.display_assignments(self.list_student_assignments())

    def submit_assignment(self):
        assignments = self.get_assignment_container().get_assignments_of_student(self.email)
        self.view.display_assignments(self.list_student_assignments())
        try:
            assignment_index = int(self.view.get_assignment_number(len(assignments))) - 1
        except TypeError:
            return None
        assignment = assignments[assignment_index]
        url = self.view.get_url()
        assignment.set_url(url)
        self.assignment_dao.export_assignments(self.assignment_container.get_assignments())

    def run(self):
        self.view.display_welcome_message()

        menu_option = None
        while menu_option != '0':
            self.view.display_students_menu()
            menu_option = self.view.get_menu_option()

            if menu_option == '1':
                self.view_grades()
            elif menu_option == '2':
                self.submit_assignment()

        self.view.display_goodbye_message()
