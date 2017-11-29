from user_base_model import UserBase


class Student(UserBase):

    def __init__(self, name, surname, email, phone_number, password, class_name, attendance):
        super().__init__(name, surname, email, phone_number, password)
        self.class_name = class_name
        self.attendance = attendance

    def get_class_name(self):
        return self.class_name

    def get_all_details(self):
        return [self.name, self.surname, self.email, self.phone_number, self.password, self.class_name, self.attendance]

    def set_class_name(self, new_class_name):
        self.class_name = new_class_name

    def set_attendance(self, student_attendance):
        if student_attendance == 'persence':
            self.attendance = self.attendance + "1"
        elif student_attendance == 'late':
            self.attendance = self.attendance + "2"
        elif student_attendance == 'absence':
            self.attendance = self.attendance + "0"

    # def get_avarage_attendance(self):
    #     return float((self.attendance[0] / self.attendance[1]) * 100)
