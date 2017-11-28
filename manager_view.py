from prettytable import PrettyTable


class ManagerView():

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

    def get_menu_option(self):
        menu_option = input("Option: ")
        return menu_option

    def get_mentors_data(self):
        mentors_name = input("Enter mentor's name: ")
        mentors_surname = input("Enter mentor's surname: ")
        mentors_email = input("Enter mentor's e-mail: ")
        mentors_phone = input("Enter mentor's phone: ")
        mentors_password = input("Enter mentor's password: ")

        mentors_data = (mentors_name, mentors_surname, mentors_email, mentors_phone, mentors_password)
        return mentors_data

    def get_mentors_email(self):
        mentors_email = input("Enter mentor's e-mail: ")
        return mentors_email

    def display_goodbye_message(self):
        print('\nGoodbye!')

    def display_message(self, message):
        print('\n' + message + '\n')

    def get_mentor_number(self, mentor_list_length):
        correct_choices = [str(n) for n in range(1, mentor_list_length + 1)]
        user_input = input("Choose mentor to remove (by number): ")
        while user_input not in correct_choices:
            print('Wrong input!')
            user_input = input("Choose mentor to remove (by number): ")
        return user_input

    def display_mentors(self, mentors_collection):
        my_table = PrettyTable(["No.", "NAME", "SURNAME", "E-MAIL", "PHONE"])
        for mentor in mentors_collection:
            my_table.add_row(mentor)
        print(my_table)
