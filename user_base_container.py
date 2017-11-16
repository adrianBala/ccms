from user_base_dao import UserBaseDao


class UserBaseContainer():

    def __init__(self):
        self.login_info = []

    def set_login_info(self, login_info):
        self.login_info = login_info

    def get_login_info(self):
        return self.login_info
