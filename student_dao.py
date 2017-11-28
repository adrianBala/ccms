import csv
from student_model import Student

class StudentDao():

    students_file = 'students.csv'

    def import_students(self):
        students = []
        with open(self.students_file, "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                student = Student(*row)
                students.append(student)
        return students
