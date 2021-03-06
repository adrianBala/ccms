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
        self.attendance = self.attendance + student_attendance

    def get_avarage_attendance(self):
        attendance_data = self.attendance
        full_attendance = len(self.attendance)
        current_attendance = self.attendance.count('1')
        attendance_but_late = self.attendance.count('2')
        late_multiplier = 0.8
        try:
            attendance_value = ((current_attendance + attendance_but_late * late_multiplier) / full_attendance) * 100
        except ZeroDivisionError:
            attendance_value = 0
        return round(attendance_value, 2)
