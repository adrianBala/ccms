class UserBase():

    def __init__(self, name, surname, email, phone_number, password):
        self.name = name
        self.surname = surname
        self.email = email
        self.phone_number = phone_number
        self.password = password

    def change_email(self, new_email):
        self.email = new_email

    def change_phone_number(self, new_phone_number):
        self. phone_number = new_phone_number

    def change_password(self, new_password):
        self.password = new_password
