from user_base_model import UserBase


class Student(UserBase):

    def __init__(self, name, surname, email, phone_number, password, class_name):
        super().__init__(name, surname, email, phone_number, password)
        self.class_name = class_name
