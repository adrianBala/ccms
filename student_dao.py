import csv
from student_model import Student

class StudentDao():

    students_file = 'students.csv'

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
