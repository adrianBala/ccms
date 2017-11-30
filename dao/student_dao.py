import csv

from model.student_model import Student


class StudentDao():

    students_file = 'students.csv'

    def create_student(self, name, surname, email, phone, password, class_name, attendance):
        return Student(name, surname, email, phone, password, class_name, attendance)

    def import_students(self):
        students = {}

        with open(self.students_file, "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                student = self.create_student(*row)
                class_name = student.get_class_name()

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
                    writer.writerow(student.get_all_details())
