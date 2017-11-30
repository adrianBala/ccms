import os

from getpass import getpass


class UserBaseView():

    def get_email(self):
        os.system('clear')
        user_email = input('Enter e-mail: ')
        return user_email

    def get_password(self):
        user_password = getpass('Enter password or E to exit: ')
        if user_password.lower() == 'e':
            exit()
        return user_password

    def display_text(self, text):
        print(text)
