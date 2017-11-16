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
        print('What would you like to do?')

    def get_menu_option(self):
        menu_option = input("Enter a number: ")
        return menu_option

    def get_students_data_from_user(self):
        students_name = input("Enter student's name: ")
        students_surname = input("Enter student's surname: ")
        students_email = input("Enter student's e-mail: ")
        students_phone = input("Enter student's phone: ")
        students_password = input("Enter student's password: ")
        students_class = input("Enter student's class: ")

        students_data = (students_name, students_surname, students_email, students_phone, students_password, students_class)
        return students_data  # zwraca tuplę
        
    def get_students_email(self):
        students_email = input("Enter student's e-mail: ")
        return students_email
    
