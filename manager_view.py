import hashlib, uuid
import re
import string

from getpass import getpass
from prettytable import PrettyTable
from user_base_container import UserBaseContainer
from user_base_dao import UserBaseDao


class ManagerView():

    def __init__(self):
        self.container = UserBaseContainer()
        self.dao = UserBaseDao()

    def display_welcome_message(self):
        print('\nWelcome!')

    def display_managers_menu(self):
        print("\nWhat would you like to do?")
        options = ('(1) List mentors',
                   '(2) List students',
                   '(3) Add mentor',
                   '(4) Remove mentor',
                   '(5) Edit mentor',
                   '(0) Exit CcMS')

        for option in options:
            print('\t' + option)

    def display_edit_mentor_menu(self):
        print("\nWhat would you like to do?")
        options = ('(1) Change mentor\'s name',
                   '(2) Change mentor\'s surname',
                   '(3) Change mentor\'s email',
                   '(4) Change mentor\'s phone number',
                   '(5) Change mentor\'s password',
                   '(0) Exit editing mentor\'s data')

        for option in options:
            print('\t' + option)

    def get_menu_option(self):
        correct_choices = ('0', '1', '2', '3', '4', '5')
        menu_option = input("Option: ")
        while menu_option not in correct_choices:
            print('Wrong input!')
            menu_option = input("Option: ")

        return menu_option

    def get_mentors_data(self):
        mentors_name = self.get_name_or_surname('name')
        mentors_surname = self.get_name_or_surname('surname')
        mentors_email = self.get_checked_email()
        mentors_phone = self.get_tel_number()
        mentors_password = self.get_password()

        mentors_data = (mentors_name, mentors_surname, mentors_email,
                        mentors_phone, self.hash_password(mentors_password))
        return mentors_data

    def get_name_or_surname(self, name_or_surname):
        user_input = input("Enter mentor's {}: ".format(name_or_surname))
        while len(user_input) == 0 or user_input.isspace():
            print('\nWrong input. Enter at least one character.')
            user_input = input("Enter mentor's {}: ".format(name_or_surname))

        return user_input

    def get_email(self):
        email = input("Enter mentor's e-mail: ")
        pattern = re.compile(r'[a-zA-Z0-9-_]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
        while not pattern.match(email):
            print('\nWrong input. Enter email in format: "x@x.x".')
            email = input("Enter mentor's e-mail: ")

        return email

    def get_tel_number(self):
        valid_chars = string.digits + '+()-'
        telnumber = input("Enter mentor's phone: ")
        while not all(x in valid_chars for x in telnumber) or sum(c.isdigit() for c in telnumber) < 9:
            print('\nWrong input. Enter digits and "+()-".')
            telnumber = input("Enter mentor's phone: ")
            print('\nWrong input. Enter digits or "+()-".')
        return telnumber

    def create_password(self, txt):
        new_password = getpass(txt)
        while len(new_password) == 0 or new_password.isspace():
            print('\nWrong input. Enter at least one character.')
            new_password = getpass(txt)

        return new_password

    def get_password(self):
        new_password = self.create_password("Enter mentor's password: ")
        retyped_new_password = self.create_password("Retype mentors's password: ")
        while new_password != retyped_new_password:
            print('\nTyped inputs are incorrects. Try again.')
            new_password = self.create_password("Enter mentor's password: ")
            retyped_new_password = self.create_password("Retype mentors's password: ")

        return new_password

    def display_list(self, collection):
        length_collection_element = 5
        if len(collection[0]) == length_collection_element:
            my_table = PrettyTable(["No.", "NAME", "SURNAME", "E-MAIL", "PHONE"])
        else:
            my_table = PrettyTable(["No.", "NAME", "SURNAME", "E-MAIL", "PHONE", "CLASS"])

        for user in collection:
            my_table.add_row(user)
        print(my_table)

    def get_mentor_number(self, mentor_list_length):
        correct_choices = [str(n) for n in range(1, mentor_list_length + 1)]
        user_input = input("Choose mentor (by number): ")
        while user_input not in correct_choices:
            print('Wrong input!')
            user_input = input("Choose mentor (by number): ")
        return user_input

    def hash_password(self, password):
        hashed_password = hashlib.sha512(password.encode('utf-8')).hexdigest()

        return hashed_password

    def display_message(self, message):
        print('\n' + message + '\n')

    def display_goodbye_message(self):
        print('\nGoodbye!')

    def get_checked_email(self):
        login_info = self.dao.import_login_info()
        self.container.set_login_info(login_info)

        email_index = 0
        checked_emails_data = False
        email = self.get_email()
        while not checked_emails_data:
            for element in login_info:
                if email == element[email_index]:
                    print('\nEmail already exist. Try a new one.')
                    self.get_email()
                    continue

            checked_emails_data = True

        return email
