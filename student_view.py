from prettytable import PrettyTable


class StudentView():

    def display_welcome_message(self):
        print('\nWelcome!')

    def display_students_menu(self):
        print('\nWhat would you like to do?')
        options = ('(1) View grades',
                   '(2) Submit assignment',
                   '(0) Exit CcMS')
        for option in options:
            print('\t' + option)

    def get_menu_option(self):
        correct_choices = ('0', '1', '2')
        menu_option = input("Option: ")
        while menu_option not in correct_choices:
            print('Wrong input!')
            menu_option = input("Option: ")
        return menu_option

    def display_goodbye_message(self):
        print('\nGoodbye!')

    def display_grades(self, collection):
        my_table = PrettyTable(["No.", "NAME", "URL", "GRADE"])
        for assignment in collection:
            my_table.add_row(assignment)
        print(my_table)
