import os

from assignment_container import AssignmentContainer
from assignment_dao import AssignmentDao
from mentor_view import MentorView
from student_container import StudentContainer
from student_dao import StudentDao


class MentorController():

    def __init__(self, user_base_dao, user_base_container):
        self.view = MentorView()
        self.student_dao = StudentDao()
        self.assignment_dao = AssignmentDao()
        self.user_base_dao = user_base_dao
        self.user_base_container = user_base_container

    def get_student_container(self):
        try:
            return self.student_container
        except AttributeError:
            self.student_container = StudentContainer()
            students = self.student_dao.import_students()
            self.student_container.set_students(students)
        return self.student_container

    def get_assignment_container(self):
        try:
            return self.assignment_container
        except AttributeError:
            self.assignment_container = AssignmentContainer()
            assignments = self.assignment_dao.import_assignments()
            self.assignment_container.set_assignments(assignments)
        return self.assignment_container

    def list_students(self, class_name=None):
        if class_name:
            students = self.get_student_container().get_students_of_class(class_name)
        else:
            students = self.get_student_container().get_all_students()
        students.sort(key=lambda student: student.get_class_name())

        students_data_collection = []
        for count, student in enumerate(students, 1):
                student_data = [count, student.get_name(), student.get_surname(),
                                student.get_email(), student.get_phone_number(), student.get_class_name()]
                students_data_collection.append(student_data)

        self.view.display_list(students_data_collection)

    def add_student(self):
        students_data = self.view.get_students_data()
        attendance = ''

        student = self.student_dao.create_student(*students_data, attendance)
        self.get_student_container().add_student(student, student.get_class_name())
        students = self.get_student_container().get_students()
        self.student_dao.export_students(students)

        self.user_base_container.add_user(student.get_email(), student.get_password(), 'student')
        login_info = self.user_base_container.get_login_info()
        self.user_base_dao.export_login_info(login_info)

        self.view.display_message("Student added!")

    def remove_student(self):
        class_names = self.get_student_container().get_class_names()
        class_name = self.view.get_class_name(class_names)

        students_of_class = self.get_student_container().get_students_of_class(class_name)
        self.list_students(class_name)
        index = int(self.view.get_student_number(len(students_of_class))) - 1
        student = self.get_student_container().pop_student(class_name, index)
        self.student_dao.export_students(self.get_student_container().get_students())

        self.user_base_container.remove_user(student.get_email())
        login_info = self.user_base_container.get_login_info()
        self.user_base_dao.export_login_info(login_info)

        self.get_assignment_container().remove_assignments(student.get_email())
        self.assignment_dao.export_assignments(self.assignment_container.get_assignments())

        self.view.display_message("Student removed!")

    def edit_student(self):
        self.list_students()

        students = self.get_student_container().get_all_students()
        index = int(self.view.get_student_number(len(students))) - 1
        student = students[index]

        menu_option = None
        while menu_option != '0':
            self.view.display_edit_student_menu()
            menu_option = self.view.get_menu_option()

            if menu_option == '1':
                new_name = self.view.get_name_or_surname('name')
                student.set_name(new_name)
            elif menu_option == '2':
                new_surname = self.view.get_name_or_surname('surname')
                student.set_surname(new_surname)
            elif menu_option == '3':
                new_email = self.view.get_email()
                old_email = student.get_email()
                student.set_email(new_email)
                self.get_assignment_container().change_email(old_email, new_email)
                self.assignment_dao.export_assignments(self.get_assignment_container().get_assignments())
            elif menu_option == '4':
                new_phone_number = self.view.get_tel_number()
                student.set_phone_number(new_phone_number)
            elif menu_option == '5':
                new_password = self.view.get_students_password()
                student.set_password(new_password)
            elif menu_option == '6':
                old_class = student.get_class_name()
                self.get_student_container().remove_student(student, old_class)

                new_class = self.view.get_students_class()
                student.set_class_name(new_class)
                self.get_student_container().add_student(student, new_class)

        self.student_dao.export_students(self.get_student_container().get_students())
        self.user_base_container.remove_user(student.get_email())
        self.user_base_container.add_user(student.get_email(), student.get_password(), 'student')
        login_info = self.user_base_container.get_login_info()
        self.user_base_dao.export_login_info(login_info)

        self.view.display_message("Student\'s data has been updated!")

    def add_assignment(self):
        class_name = self.view.get_class_name(self.get_student_container().get_class_names())
        assignment_name = self.view.get_assignment_name()

        students = self.get_student_container().get_students_of_class(class_name)
        for student in students:
            assignment = self.assignment_dao.create_assignment(student.get_email(), assignment_name)
            self.get_assignment_container().add_assignment(assignment)
        self.assignment_dao.export_assignments(self.assignment_container.get_assignments())

    def list_student_assignments(self, email):
        assignments_data_collection = []

        student_assignments = self.get_assignment_container().get_assignments_of_student(email)
        for count, assignment in enumerate(student_assignments, 1):
            assignment_data = [count, assignment.get_name(), assignment.get_url(),
                               assignment.get_grade()]
            assignments_data_collection.append(assignment_data)

        self.view.display_assignments(assignments_data_collection)

    def grade_assignment(self):
        self.list_students()

        students = self.get_student_container().get_all_students()
        student_index = int(self.view.get_student_number(len(students))) - 1
        student = students[student_index]
        email = student.get_email()
        student_assignments = self.get_assignment_container().get_assignments_of_student(email)
        self.list_student_assignments(email)
        try:
            assignment_index = int(self.view.get_assignment_number(len(student_assignments))) - 1
        except TypeError:
            return None
        assignment = student_assignments[assignment_index]
        self.view.display_message('Assignment url: {}'.format(assignment.get_url()))
        grade = self.view.get_grade()
        assignment.set_grade(grade)
        self.assignment_dao.export_assignments(self.assignment_container.get_assignments())

    def check_attendance(self):
        class_names = self.get_student_container().get_class_names()
        class_name = self.view.get_class_name(class_names)
        self.list_students(class_name)

        students_of_class = self.get_student_container().get_students_of_class(class_name)
        for student in students_of_class:
            name = student.get_name()
            surname = student.get_surname()
            student_attendance = self.view.get_attendance(name, surname)
            late = '2'
            absence = '0'
            persence = '1'
            if student_attendance == 'Y':
                student_attendance_type = persence
            elif student_attendance == 'N':
                student_attendance_type = absence
            elif student_attendance == 'L':
                student_attendance_type = late
            student.set_attendance(student_attendance_type)
            self.student_dao.export_students(self.get_student_container().get_students())
            attendance_value = student.get_avarage_attendance()
            self.view.display_attendance_value(name, surname, attendance_value)

    def check_attendance_of_class(self):
        class_names = self.get_student_container().get_class_names()
        class_name = self.view.get_class_name(class_names)

        students_of_class = self.get_student_container().get_students_of_class(class_name)
        for student in students_of_class:
            name = student.get_name()
            surname = student.get_surname()
            attendance_value = student.get_avarage_attendance()
            self.view.display_attendance_value(name, surname, attendance_value)

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
            elif menu_option == '8':
                self.check_attendance_of_class()

        self.view.display_goodbye_message()
