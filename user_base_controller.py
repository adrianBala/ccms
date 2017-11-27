from user_base_model import UserBase
from user_base_dao import UserBaseDao
from user_base_view import UserBaseView
from user_base_container import UserBaseContainer


class UserBaseController():

    def __init__(self):
        self.view = UserBaseView()
        self.dao = UserBaseDao()
        self.container = UserBaseContainer()

    def validate_password(self, email, password, user_email, user_password):
        return email == user_email and password == user_password

    def sign_in(self):
        signed_in = False
        while not signed_in:
            user_email = self.view.get_email()
            user_password = self.view.get_password()

            login_info = self.dao.import_login_info()
            self.container.set_login_info(login_info)

            for row in self.container.get_login_info():
                email, password, status = row
                if self.validate_password(email, password, user_email, user_password):
                    return email, status
            self.view.display_text('Access denied!')
