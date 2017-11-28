from user_base_model import UserBase


class Student(UserBase):

    def __init__(self, name, surname, email, phone_number, password, class_name):
        super().__init__(name, surname, email, phone_number, password)
        self.class_name = class_name

    def get_class_name(self):
        return self.class_name

    def set_class_name(self, new_class_name):
        self.class_name = new_class_name
