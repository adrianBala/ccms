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

    def display_assignments(self, collection):
        my_table = PrettyTable(["No.", "NAME", "URL", "GRADE"])
        for assignment in collection:
            my_table.add_row(assignment)
        print(my_table)

    def get_assignment_number(self, assignment_list_length):
        correct_choices = [str(n) for n in range(1, assignment_list_length + 1)]
        user_input = input("Choose assignment (by number) or E to exit: ")
        while user_input not in correct_choices and user_input.lower() != "e":
            print('Wrong input!')
            user_input = input("Choose assignment (by number): ")
        if user_input.lower() == "e":
            return None
        return user_input

    def get_url(self):
        user_input = input("Enter url: ")
        while len(user_input) == 0 or user_input.isspace():
            print('\nWrong input. Enter at least one character.')
            user_input = input("Enter url: ")
        return user_input
