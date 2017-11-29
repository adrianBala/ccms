import re
import string
from prettytable import PrettyTable


class MentorView():

    def display_welcome_message(self):
        print('\nWelcome!')

    def display_mentors_menu(self):
        print('\nWhat would you like to do?')
        options = ('(1) List students',
                   '(2) Add student',
                   '(3) Remove student',
                   '(4) Edit student',
                   '(5) Add assignment',
                   '(6) Grade assignment',
                   '(7) Check attendance',
                   '(0) Exit CcMS')
        for option in options:
            print('\t' + option)

    def display_edit_student_menu(self):
        print("\nWhat would you like to do?")
        options = ('(1) Change student\'s name',
                   '(2) Change student\'s surname',
                   '(3) Change student\'s email',
                   '(4) Change student\'s phone number',
                   '(5) Change student\'s password',
                   '(6) Change student\'s class',
                   '(0) Exit editing student\'s data')

        for option in options:
            print('\t' + option)

    def get_menu_option(self):
        menu_option = input("Option: ")
        return menu_option

    def get_students_data(self):
        students_name = self.get_name_or_surname('name')
        students_surname = self.get_name_or_surname('surname')
        students_email = self.get_email()
        students_phone = self.get_tel_number()
        students_password = self.get_password()
        students_class = self.get_students_class()

        students_data = (students_name, students_surname, students_email, students_phone, students_password, students_class)
        return students_data

    def get_name_or_surname(self, name_or_surname):
        user_input = input("Enter student's {}: ".format(name_or_surname))
        while len(user_input) == 0 or user_input.isspace():
            print('\nWrong input. Enter at least one character.')
            user_input = input("Enter student's {}: ".format(name_or_surname))

        return user_input

    def get_email(self):
        email = input("Enter e-mail: ")
        pattern = re.compile(r'[a-zA-Z0-9-_]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
        while not pattern.match(email):
            print('\nWrong input. Enter email in format: "x@x.x".')
            email = input("Enter e-mail: ")

        return email

    def get_tel_number(self):
        valid_chars = string.digits + '+()-'
        telnumber = input("Enter student's phone: ")
        while not all(x in valid_chars for x in telnumber) or sum(c.isdigit() for c in telnumber) < 9:
            print('\nWrong input. Enter digits and "+()-".')
            telnumber = input("Enter mentor's phone: ")

        return telnumber

    def get_password(self):
        user_input = input("Enter student's password: ")
        while len(user_input) == 0 or user_input.isspace():
            print('\nWrong input. Enter at least one character.')
            user_input = input("Enter student's password: ")

        return user_input

    def get_students_class(self):
        students_class = input("Enter student's class: ")
        while len(students_class) != 2 or not students_class[0].isdigit() or not students_class[1].isalpha():
            print('\nWrong input. Enter class in format: "XY", where "X" is a single digit and "Y" is a single letter.')
            students_class = input("Enter student's class: ")

        return students_class[0] + students_class[1].lower()

    def display_list(self, collection):
        my_table = PrettyTable(["No.", "NAME", "SURNAME", "E-MAIL", "PHONE", "CLASS"])
        for user in collection:
            my_table.add_row(user)
        print(my_table)

    def get_student_number(self, student_list_length):
        correct_choices = [str(n) for n in range(1, student_list_length + 1)]
        user_input = input("Choose student (by number): ")
        while user_input not in correct_choices:
            print('Wrong input!')
            user_input = input("Choose student (by number): ")
        return user_input

    def get_class_name(self, class_names):
        class_name = ''
        while class_name not in class_names:
            print("Available classes: {}".format(', '.join(class_names)))
            class_name = input('Select class: ')
        return class_name

    def get_attendance(self, name, surname):
        attendance = None
        while attendance not in ['Y', 'N', 'L']:
            print('Is {} {} with us?'.format(name, surname))
            attendance = input('Enter Yes or No(Y/N/L): ').upper()
        if attendance == 'Y':
            return 'persence'
        elif attendance == 'N':
            return 'absence'
        elif attendance == 'L':
            return 'late'

    def display_attendance_value(self, name, surname, attendance_vlaue):
        return print('{} {} presence is: {}%'.format(name, surname, attendance_vlaue))

    def display_message(self, message):
        print('\n' + message + '\n')

    def display_goodbye_message(self):
        print('\nGoodbye!')
