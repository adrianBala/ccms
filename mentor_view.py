class MentorView():

    def display_welcome_message(self):
        print('\nWelcome!')

    def display_mentors_menu(self):
        print('\nWhat would you like to do?')
        options = ('(1) List students',
                   '(2) Add student',
                   '(3) Remove student',
                   '(4) Edit student',
                   '(5) Add assignment',
                   '(6) Grade assignment',
                   '(7) Check attendance',
                   '(0) Exit CcMS')
        for option in options:
            print('\t' + option)

    def get_menu_option(self):
        menu_option = input("Option: ")
        return menu_option

    def get_students_data_from_user(self):
        students_name = input("Enter student's name: ")
        students_surname = input("Enter student's surname: ")
        students_email = input("Enter student's e-mail: ")
        students_phone = input("Enter student's phone: ")
        students_password = input("Enter student's password: ")
        students_class = input("Enter student's class: ")

        students_data = (students_name, students_surname, students_email, students_phone, students_password, students_class)
        return students_data

    def get_students_email(self):
        students_email = input("Enter student's e-mail: ")
        return students_email

    def display_goodbye_message(self):
        print('\nGoodbye!')

    def display_message(self, message):
        print('\n' + message + '\n')

    def get_class_name(self, class_names):
        class_name = ''
        while class_name not in class_names:
            print("Available classes: {}".format(', '.join(class_names)))
            class_name = input('Select class: ')
            return class_name

    def get_student_number(self, student_list_length):
        correct_choices = [str(n) for n in range(1, len(student_list_length) + 1)]
        user_input = input("Choose student to remove (by number): ")
        while user_input not in correct_choices:
            print('Wrong input!')
            user_input = input("Choose student to remove (by number): ")
        return user_input
