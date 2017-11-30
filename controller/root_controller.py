from controller.manager_controller import ManagerController
from controller.mentor_controller import MentorController
from controller.regular_employee_controller import RegularEmployeeController
from controller.student_controller import StudentController
from controller.user_base_controller import UserBaseController


class RootController():

    def __init__(self):
        self.user_base_controller = UserBaseController()

    def start(self):
        email, status = self.user_base_controller.sign_in()

        user_base_dao = self.user_base_controller.get_dao()
        user_base_container = self.user_base_controller.get_container()

        if status == 'manager':
            self.controller = ManagerController(user_base_dao, user_base_container)
        elif status == 'mentor':
            self.controller = MentorController(user_base_dao, user_base_container)
        elif status == 'regular_employee':
            self.controller = RegularEmployeeController()
        elif status == 'student':
            self.controller = StudentController(email)

        self.controller.run()
