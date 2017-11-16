class RegularEmployeeView():

    def display_employees_menu(self):
        options = ('(1) List students',
                   '(0) Exit CcMS')
        for option in options:
            print(option)
        print('What would you like to do?')

    def get_menu_option(self):
        menu_option = input("Enter a number: ")
        return menu_option


    

