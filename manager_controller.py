from manager_view import ManagerView
from mentor_dao import MentorDao
from student_dao import StudentDao
from mentor_container import MentorContainer

class ManagerController():

    def __init__(self):
        self.view = ManagerView()
        self.mentor_dao = MentorDao()
        self.student_dao = StudentDao()

    def get_list_of students(self):
        return self.student_dao.import_students()

    def get_mentor_container(self):
        try:
            return self.mentor_container
        except AttributeError:
            self.mentor_container = MentorContainer()
            self.mentor_container.import_mentors()
        return self.mentor_container

    def add_mentor(self):
        mentor_data = self.view.get_mentors_data()
        mentor = self.mentor_dao.create_mentor(mentor_data)
        self.get_mentor_container.add_mentor(mentor)
        mentors = self.get_mentor_container().get_mentors()
        self.mentor_dao.export_mentors(mentors)
