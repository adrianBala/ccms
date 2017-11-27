from prettytable import PrettyTable

class ManagerView():

    def __init__(self):
        self.mentors_collection = []


    def display_managers_menu(self):
        options = ('(1) List mentors',
                   '(2) List students',
                   '(3) Add mentor',
                   '(4) Remove mentor',
                   '(5) Edit mentor',
                   '(0) Exit CcMS')

        for option in options:
            print(option)
        print("What would you like to do?")

    def get_menu_option(self):
        menu_option = input("Enter a number: ")
        return menu_option

    def get_mentors_data(self):
        mentors_name = input("Enter mentor's name: ")
        mentors_surname = input("Enter mentor's surname: ")
        mentors_email = input("Enter mentor's e-mail: ")
        mentors_phone = input("Enter mentor's phone: ")
        mentors_password = input("Enter mentor's password: ")

        mentors_data = (mentors_name, mentors_surname, mentors_email, mentors_phone, mentors_password)
        return mentors_data  # zwraca tuplę

    def get_mentors_email(self):
        mentors_email = input("Enter mentor's e-mail: ")
        return mentors_email

    def display_mentors(self):
        my_table = PrettyTable(["NAME", "SURNAME", "E-MAIL", "PHONE"])
        for mentor in self.mentors_collection:
            my_table.add_row(mentor)
        print(my_table)
        input("\nPress Enter to go back")

        
