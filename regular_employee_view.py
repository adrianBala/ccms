from prettytable import PrettyTable


class RegularEmployeeView():

    def display_welcome_message(self):
        print('\nWelcome!')

    def display_employees_menu(self):
        print('\nWhat would you like to do?')
        options = ('(1) List students',
                   '(0) Exit CcMS')
        for option in options:
            print('\t' + option)

    def get_menu_option(self):
        correct_choices = ('0', '1')
        menu_option = input("Option: ")
        while menu_option not in correct_choices:
            print('Wrong input!')
            menu_option = input("Option: ")
        return menu_option

    def display_list(self, collection):
        my_table = PrettyTable(["No.", "NAME", "SURNAME", "E-MAIL", "PHONE", "CLASS"])
        for user in collection:
            my_table.add_row(user)
        print(my_table)

    def display_goodbye_message(self):
        print('\nGoodbye!')

    def display_continue_key(self):
        return input('Press Enter to continue')
