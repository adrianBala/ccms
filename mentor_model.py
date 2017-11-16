from user_base_model import UserBase


class Mentor(UserBase):

    def __init__(self, name, surname, email, phone_number, password):
        super().__init__(name, surname, email, phone_number, password)
