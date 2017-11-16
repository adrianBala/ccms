from manager_view import ManagerView
from mentor_dao import MentorDao
from student_dao import StudentDao
from mentor_container import MentorContainer

class ManagerController():

    def __init__(self):
        self.view = ManagerView()
        self.mentor_dao = MentorDao()
        self.student_dao = StudentDao()

    def list_mentors(self):
        mentors = self.get_mentor_container().get_mentors()
        for mentor in mentors:
            print(mentor)  #to be changed

    def get_mentor_container(self):
        try:
            return self.mentor_container
        except AttributeError:
            self.mentor_container = MentorContainer()
            mentors = self.mentor_dao.import_mentors()
            self.mentor_container.set_mentors(mentors)
        return self.mentor_container

    def add_mentor(self):
        mentor_data = self.view.get_mentors_data()
        mentor = self.mentor_dao.create_mentor(*mentor_data)
        self.get_mentor_container().add_mentor(mentor)
        mentors = self.get_mentor_container().get_mentors()
        self.mentor_dao.export_mentors(mentors)

    def start(self):
        while True:
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
