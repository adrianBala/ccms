from mentor_dao import MentorDao
from student_dao import StudentDao

class ManagerController():

    def __init__(self):
        self.view = ManagerView()
        self.mentor_dao = MentorDao()

    def get_list_of mentors(self):
        return self.mentor_dao.import_mentors()
