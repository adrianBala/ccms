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
        students_email = self.get_students_email()
        students_phone = self.get_tel_number()
        students_password = self.get_students_password()
        students_class = self.get_students_class()

        students_data = (students_name, students_surname, students_email, students_phone, students_password, students_class)
        return students_data

    def get_students_email(self):
        students_email = input("Enter student's e-mail: ")
        return students_email

    def display_goodbye_message(self):
        print('\nGoodbye!')

    def display_message(self, message):
        print('\n' + message + '\n')

    def display_list(self, collection):
        my_table = PrettyTable(["No.", "NAME", "SURNAME", "E-MAIL", "PHONE", "CLASS"])
        for user in collection:
            my_table.add_row(user)
        print(my_table)

    def get_name_or_surname(self, name_or_surname):
        loop_is_running = True
        while loop_is_running:
            user_input = input("Enter student's {}: ".format(name_or_surname))
            if len(user_input) != 0:
                if user_input.isspace():
                    print('\nWrong input. Enter at least one "nonspace" letter.')

                    continue

                return user_input

            print('\nWrong input. Enter at least one character.')

    def get_students_email(self):
        valid_chars = string.ascii_lowercase + string.digits + '.'
        valid_chars_plus = string.ascii_lowercase + string.digits + '_.-'
        loop_is_running = True
        while loop_is_running:
            email = input("Enter student's e-mail: ")
            if len(email) >= 5 and email.isspace() == False and '@' in email and '.' in email:
                chars_to_monkey = email.split('@')[0]
                chars_after_monkey = email.split('@')[1]
                if chars_after_monkey.count('.') > 0:
                    chars_before_last_dot = chars_after_monkey.split('.')[0]
                    chars_after_last_dot = chars_after_monkey.split('.')[1]
                    if len(chars_before_last_dot) >= 1 and len(chars_after_last_dot) >= 1:
                        if all(x in valid_chars_plus for x in chars_to_monkey):
                            if all(x in valid_chars for x in chars_after_monkey):

                                return email

            print('\nWrong input. Enter email in format: "x@x.x".')

    def get_tel_number(self):
        valid_chars = string.digits + '+()-'
        loop_is_running = True
        while loop_is_running:
            telnumber = input("Enter mentor's phone: ")
            if all(x in valid_chars for x in telnumber):
                if sum(c.isdigit() for c in telnumber) >= 9:

                    return telnumber

                print('\nWrong input. Enter at least 9 digits.')
                continue

            print('\nWrong input. Enter digits and "+()-".')

    def get_students_class(self):
        loop_is_running = True
        while loop_is_running:
            students_class = input("Enter student's class: ")
            if len(students_class) == 2 and students_class[0].isdigit() and students_class[1].isalpha():
                result = students_class[0] + students_class[1].upper()
                return result

            print('\nWrong input. Enter class in format: "XY", where "X" is a single digit and "Y" is a single letter.')

    def get_class_name(self, class_names):
        class_name = ''
        while class_name not in class_names:
            print("Available classes: {}".format(', '.join(class_names)))
            class_name = input('Select class: ')
        return class_name

    def get_student_number(self, student_list_length):
        correct_choices = [str(n) for n in range(1, student_list_length + 1)]
        user_input = input("Choose student (by number): ")
        while user_input not in correct_choices:
            print('Wrong input!')
            user_input = input("Choose student (by number): ")
        return user_input

    def get_students_password(self):
        return input("Enter student's password: ")
