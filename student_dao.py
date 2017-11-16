import csv

class StudentDao():

    students_file = 'students.csv'

    def import_students(self):
        students = []
        with open(self.students_file, "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                students.append(row)
        return students
