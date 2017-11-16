class UserBase():

    def __init__(self, name, surname, email, phone_number, password):
        self.name = name
        self.surname = surname
        self.email = email
        self.phone_number = phone_number
        self.password = password

    def change_email(new_email):
        self.email = new_email
