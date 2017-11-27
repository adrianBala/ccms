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
        menu_option = input("Option: ")
        return menu_option

    def display_goodbye_message(self):
        print('\nGoodbye!')
