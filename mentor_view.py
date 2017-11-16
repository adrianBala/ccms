class MentorView():
    
    def display_mentors_menu(self):
        options = ('(1) List students',
                   '(2) Add student',
                   '(3) Remove student',
                   '(4) Edit student',
                   '(5) Add assignment',
                   '(6) Grade assignment',
                   '(7) Check attendance',
                   '(0) Exit CcMS')
        for option in options:
            print(option)
        print('What would you like to do: ')

    def get_menu_option(self):
        menu_option = input("Enter a number: ")
        return menu_option

    
