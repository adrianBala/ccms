from user_base_model import UserBase


class Student(UserBase):

    def __init__(self, name, surname, email, phone_number, password):
        super().__init(name, surname, email, phone_nubmer, password)
