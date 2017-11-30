from dao.user_base_dao import UserBaseDao


class UserBaseContainer():

    def __init__(self):
        self.login_info = []

    def get_login_info(self):
        return self.login_info

    def set_login_info(self, login_info):
        self.login_info = login_info

    def add_user(self, login, password, status):
        self.login_info.append([login, password, status])

    def remove_user(self, email):
        email_index = 0
        for login in self.login_info:
            if login[email_index] == email:
                self.login_info.remove(login)
                break
