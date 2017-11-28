import string

class MentorView():

    def display_mentors_menu(self):
        options = ('(1) List students',
                   '(2) Add student',
                   '(3) Remove student',
                   '(4) Edit student',
                   '(5) Add assignment',
                   '(6) Grade assignment',
                   '(7) Check attendance',
                   '(0) Exit CcMS')
        for option in options:
            print(option)
        print('What would you like to do?')

    def get_menu_option(self):
        menu_option = input("Enter a number: ")
        return menu_option

    def get_students_data_from_user(self):
        students_name = self.get_name_or_surname('name')
        students_surname = self.get_name_or_surname('surname')
        students_email = self.get_students_email()
        students_phone = self.get_tel_number()
        students_password = input("Enter student's password: ")
        students_class = self.get_students_class()

        students_data = (students_name, students_surname, students_email,
                         students_phone, students_password, students_class)
        return students_data  # zwraca tuplę

    def get_name_or_surname(self, name_or_surname):
        while True:
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
        while True:
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
        while True:
            telnumber = input("Enter mentor's phone: ")
            if all(x in valid_chars for x in telnumber):
                if sum(c.isdigit() for c in telnumber) >= 9:

                    return telnumber

                print('\nWrong input. Enter at least 9 digits.')
                continue

            print('\nWrong input. Enter digits and "+()-".')

    def get_students_class(self):
        while True:
            students_class = input("Enter student's class: ")
            if len(students_class) == 2 and students_class[0].isdigit() and students_class[1].isalpha():
                result = students_class[0] + students_class[1].upper()
                return result

            print('\nWrong input. Enter class in format: "XY", where "X" is a single digit and "Y" is a single letter.')
