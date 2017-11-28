import string

class ManagerView():

    def display_managers_menu(self):
        options = ('(1) List mentors',
                   '(2) List students',
                   '(3) Add mentor',
                   '(4) Remove mentor',
                   '(5) Edit mentor',
                   '(0) Exit CcMS')

        for option in options:
            print(option)
        print("What would you like to do?")

    def get_menu_option(self):
        menu_option = input("Enter a number: ")
        return menu_option

    def get_mentors_data(self):
        mentors_name = self.get_name_or_surname('name')
        mentors_surname = self.get_name_or_surname('surname')
        mentors_email = self.get_mentors_email()
        mentors_phone = self.get_tel_number()
        mentors_password = input("Enter mentor's password: ")

        mentors_data = (mentors_name, mentors_surname, mentors_email, mentors_phone, mentors_password)
        return mentors_data  # zwraca tuplę

    def get_name_or_surname(self, name_or_surname):
        loop_is_running = True
        while loop_is_running:
            user_input = input("Enter mentor's {}: ".format(name_or_surname))
            if len(user_input) != 0:
                if user_input.isspace():
                    print('\nWrong input. Enter at least one "nonspace" letter.')

                    continue

                return user_input

            print('\nWrong input. Enter at least one character.')

    def get_mentors_email(self):
        valid_chars = string.ascii_lowercase + string.digits + '.'
        valid_chars_plus = string.ascii_lowercase + string.digits + '_.-'
        loop_is_running = True
        while loop_is_running:
            email = input("Enter mentor's e-mail: ")
            if len(email) => 5 and email.isspace() == False and '@' in email and '.' in email:
                chars_to_monkey = email.split('@')[0]
                chars_after_monkey = email.split('@')[1]
                if chars_after_monkey.count('.') > 0:
                    chars_before_last_dot = chars_after_monkey.split('.')[0]
                    chars_after_last_dot = chars_after_monkey.split('.')[1]
                    if len(chars_before_last_dot) => 1 and len(chars_after_last_dot) => 1:
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

            print('\nWrong input. Enter digits or "+()-".')
