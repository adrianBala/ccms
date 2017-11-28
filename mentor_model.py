from user_base_model import UserBase


class Mentor(UserBase):

    def __init__(self, name, surname, email, phone_number, password):
        super().__init__(name, surname, email, phone_number, password)

    def get_all_details(self):
        return self.name, self.surname, self.email, self.phone_number, self.password
