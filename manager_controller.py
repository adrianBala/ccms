from manager_view import ManagerView
from mentor_container import MentorContainer
from mentor_dao import MentorDao
from student_container import StudentContainer
from student_dao import StudentDao


class ManagerController():

    def __init__(self, user_base_dao, user_base_container):
        self.view = ManagerView()
        self.mentor_dao = MentorDao()
        self.student_dao = StudentDao()
        self.user_base_dao = user_base_dao
        self.user_base_container = user_base_container

    def get_mentor_container(self):
        try:
            return self.mentor_container
        except AttributeError:
            self.mentor_container = MentorContainer()
            mentors = self.mentor_dao.import_mentors()
            self.mentor_container.set_mentors(mentors)
        return self.mentor_container

    def get_student_container(self):
        try:
            return self.student_container
        except AttributeError:
            self.student_container = StudentContainer()
            students = self.student_dao.import_students()
            self.student_container.set_students(students)
        return self.student_container

    def list_mentors(self):
        mentors = self.get_mentor_container().get_mentors()

        mentors_data_collection = []
        for count, mentor in enumerate(mentors, 1):
                mentor_data = [count, mentor.get_name(), mentor.get_surname(),
                               mentor.get_email(), mentor.get_phone_number()]
                mentors_data_collection.append(mentor_data)

        self.view.display_list(mentors_data_collection)

    def list_students(self):
        students = self.get_student_container().get_all_students()
        students.sort(key=lambda student: student.get_class_name())

        students_data_collection = []
        for count, student in enumerate(students, 1):
                student_data = [count, student.get_name(), student.get_surname(),
                                student.get_email(), student.get_phone_number(), student.get_class_name()]
                students_data_collection.append(student_data)

        self.view.display_list(students_data_collection)

    def add_mentor(self):
        mentors_data = self.view.get_mentors_data()

        mentor = self.mentor_dao.create_mentor(*mentors_data)
        self.get_mentor_container().add_mentor(mentor)
        mentors = self.get_mentor_container().get_mentors()
        self.mentor_dao.export_mentors(mentors)

        self.user_base_container.add_user(mentor.get_email(), mentor.get_password(), 'mentor')
        login_info = self.user_base_container.get_login_info()
        self.user_base_dao.export_login_info(login_info)

        self.view.display_message("Mentor added!")

    def remove_mentor(self):
        self.list_mentors()

        mentors = self.get_mentor_container().get_mentors()
        index = int(self.view.get_mentor_number(len(mentors))) - 1
        mentor = self.get_mentor_container().pop_mentor(index)
        self.mentor_dao.export_mentors(mentors)

        self.user_base_container.remove_user(mentor.get_email())
        login_info = self.user_base_container.get_login_info()
        self.user_base_dao.export_login_info(login_info)

        self.view.display_message("Mentor removed!")

    def edit_mentor(self):
        self.list_mentors()

        mentors = self.get_mentor_container().get_mentors()
        index = int(self.view.get_mentor_number(len(mentors))) - 1
        mentor = mentors[index]

        menu_option = None
        while menu_option != '0':
            self.view.display_edit_mentor_menu()
            menu_option = self.view.get_menu_option()

            if menu_option == '1':
                new_name = self.view.get_name_or_surname('name')
                mentor.set_name(new_name)
            elif menu_option == '2':
                new_surname = self.view.get_name_or_surname('surname')
                mentor.set_surname(new_surname)
            elif menu_option == '3':
                new_email = self.view.get_mentors_email()
                mentor.set_email(new_email)
            elif menu_option == '4':
                new_phone_number = self.view.get_tel_number()
                mentor.set_phone_number(new_phone_number)
            elif menu_option == '5':
                new_password = self.view.get_mentors_password()
                mentor.set_password(new_password)

        self.mentor_dao.export_mentors(mentors)
        self.user_base_container.remove_user(mentor.get_email())
        self.user_base_container.add_user(mentor.get_email(), mentor.get_password(), 'mentor')
        login_info = self.user_base_container.get_login_info()
        self.user_base_dao.export_login_info(login_info)

        self.view.display_message("Mentor\'s data has been updated!")

    def run(self):
        self.view.display_welcome_message()

        menu_option = None
        while menu_option != '0':
            self.view.display_managers_menu()
            menu_option = self.view.get_menu_option()

            if menu_option == '1':
                self.list_mentors()
            elif menu_option == '2':
                self.list_students()
            elif menu_option == '3':
                self.add_mentor()
            elif menu_option == '4':
                self.remove_mentor()
            elif menu_option == '5':
                self.edit_mentor()

        self.view.display_goodbye_message()
