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
        mentors_phone = input("Enter mentor's phone: ")
        mentors_password = input("Enter mentor's password: ")

        mentors_data = (mentors_name, mentors_surname, mentors_email, mentors_phone, mentors_password)
        return mentors_data  # zwraca tuplę

    def get_name_or_surname(self, name_or_surname):
        while True:
            user_input = input("Enter mentor's {}: ".format(name_or_surname))
            if len(user_input) != 0:
                if user_input.isspace():
                    print('\nWrong input. Enter at least one "nonspace" letter.')
                    continue
                return user_input
            print('\nWrong input. Enter at least one character.')

    def get_mentors_email(self):
        while True:
            chars = string.ascii_lowercase + string.digits + '.'
            chars_plus = string.ascii_lowercase + string.digits + '_.-'
            email = input("Enter mentor's e-mail: ")
            chars_to_monkey = email.split('@')[0]
            chars_after_monkey = email.split('@')[1]
            if email.count('@') + chars_after_monkey.count('.') == 2:
                if all(x in chars_plus for x in chars_to_monkey):
                    if all(x in chars for x in chars_after_monkey):
                        return email

            print('\nWrong input. Enter email in format: "xxx@xxx.xxx".')
