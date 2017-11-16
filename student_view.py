class StudentView():

    def display_students_menu(self):
        options = ('(1) View grades',
                   '(2) Submit assignment',
                   '(0) Exit CcMS')
        for option in options:
            print(option)
        print('What would you like to do: ')

    def get_menu_option(self):
        menu_option = input("Enter a number: ")
        return menu_option
    