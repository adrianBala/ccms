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
        menu_option = input("Option: ")
        return menu_option

    def display_goodbye_message(self):
        print('\nGoodbye!')
