from mentor_dao import MentorDao
from student_dao import StudentDao

class ManagerController():

    def __init__(self):
        self.view = ManagerView()
        self.mentor_dao = MentorDao()
        self.student_dao = StudentDao()

    def get_list_of mentors(self):
        return self.mentor_dao.import_mentors()

    def get_list_of students(self):
        return self.student_dao.import_students()

    
