import csv
from student_model import Student


class StudentDao():

    students_file = 'students.csv'

    def create_student(self, name, surname, email, phone, password, class_name):
        return Student(name, surname, email, phone, password, class_name)

    def import_students(self):
        students = {}
        class_index = -1

        with open(self.students_file, "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                class_name = row[class_index]
                student = Student(*row)
                if class_name in students:
                    students[class_name].append(student)
                else:
                    students[class_name] = [student]
        return students

    def export_students(self, students):
        with open(self.students_file, "w") as csvfile:
            writer = csv.writer(csvfile)
            for students_list in students.values():
                for student in students_list:
                    name = student.get_name()
                    surname = student.get_surname()
                    email = student.get_email()
                    phone = student.get_phone_number()
                    password = student.get_password()
                    class_name = student.get_class_name()
                    writer.writerow([name, surname, email, phone, password, class_name])
