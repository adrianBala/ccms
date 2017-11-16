from user_base_controller import UserBaseController
from manager_controller import ManagerController
from mentor_controller import MentorController
from regular_employee_controller import RegularEmployeeController
from student_controller import StudentController


class RootController():

    def __init__(self):
        self.user_base_controller = UserBaseController()

    def start(self):
        email, status = self.user_base_controller.sign_in()

        if status == 'manager':
            self.controller = ManagerController()
        elif status == 'mentor':
            self.controller = MentorController()
        elif status == 'regular_employee':
            self.controller = RegularEmployeeController()
        elif status == 'student':
            self.controller = StudentController()

        self.controller.start()
