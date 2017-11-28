from manager_view import ManagerView
from mentor_dao import MentorDao
from student_dao import StudentDao
from mentor_container import MentorContainer


class ManagerController():

    def __init__(self, user_base_dao, user_base_container):
        self.view = ManagerView()
        self.mentor_dao = MentorDao()
        self.student_dao = StudentDao()
        self.user_base_dao = user_base_dao
        self.user_base_container = user_base_container

    def list_mentors(self):
        mentors = self.get_mentor_container().get_mentors()
        mentors_collection = []
        count = 1
        for mentor in mentors:
            mentor_data = [count, mentor.name, mentor.surname, mentor.email, mentor.phone_number]
            mentors_collection.append(mentor_data)
            count += 1
        self.view.display_list(mentors_collection)

    def get_mentor_container(self):
        try:
            return self.mentor_container
        except AttributeError:
            self.mentor_container = MentorContainer()
            mentors = self.mentor_dao.import_mentors()
            self.mentor_container.set_mentors(mentors)
        return self.mentor_container

    def add_mentor(self):
        mentors_data = self.view.get_mentors_data()
        mentors_name, mentors_surname, mentors_email, mentors_phone, mentors_password = mentors_data

        mentor = self.mentor_dao.create_mentor(*mentors_data)
        self.get_mentor_container().add_mentor(mentor)
        mentors = self.get_mentor_container().get_mentors()
        self.mentor_dao.export_mentors(mentors)

        self.user_base_container.add_user(mentors_email, mentors_password, 'mentor')
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

    def start(self):
        self.view.display_welcome_message()

        end = False
        while not end:
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
            elif menu_option == '0':
                end = True

        self.view.display_goodbye_message()
