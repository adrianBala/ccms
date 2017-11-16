class UserBase():

    def __init__(self, name, surname, email, phone_number, password):
        self.name = name
        self.surname = surname
        self.email = email
        self.phone_number = phone_number
        self.password = password

    def __str__(self):
        return '{} {} {} {}'.format(self.name, self.surname, self.email, self.phone_number)

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_email(self):
        return self.email

    def get_phone_number(self):
        return self.phone_number

    def get_password(self):
        return self.password

    def change_email(self, new_email):
        self.email = new_email

    def change_phone_number(self, new_phone_number):
        self. phone_number = new_phone_number

    def change_password(self, new_password):
        self.password = new_password
