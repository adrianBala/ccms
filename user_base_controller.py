import hashlib, uuid

from user_base_container import UserBaseContainer
from user_base_dao import UserBaseDao
from user_base_model import UserBase
from user_base_view import UserBaseView


class UserBaseController():

    def __init__(self):
        self.view = UserBaseView()
        self.dao = UserBaseDao()
        self.container = UserBaseContainer()

    def get_dao(self):
        return self.dao

    def get_container(self):
        return self.container

    def validate_password(self, email, password, user_email, user_password):
        if len(password) > 50:
            hashed_user_password = self.hash_password(user_password)
            return email == user_email and password == hashed_user_password
        else:
            return email == user_email and password == user_password

    def sign_in(self):
        login_info = self.dao.import_login_info()
        self.container.set_login_info(login_info)

        signed_in = False
        while not signed_in:
            user_email = self.view.get_email()
            user_password = self.view.get_password()
            for row in self.container.get_login_info():
                email, password, status = row
                if self.validate_password(email, password, user_email, user_password):
                    return email, status

            self.view.display_text('Access denied!')

    def hash_password(self, password):
        hashed_password = hashlib.sha512(password.encode('utf-8')).hexdigest()

        return hashed_password

    def get_existing_emails(self):
        login_info = self.dao.import_login_info()
        self.container.set_login_info(login_info)
        existing_emails = []

        email_index = 0
        for row in self.container.get_login_info():
            existing_emails.append(row[email_index])

        return existing_emails
