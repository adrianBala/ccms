class StudentContainer():

    def __init__(self):
        self.students = {}

    def get_students(self):
        return self.students

    def get_students_of_class(self, class_name):
        return self.students[class_name]

    def get_class_names(self):
        return [key for key in self.students]

    def set_students(self, students):
        self.students = students

    def add_student(self, student, class_name):
        if class_name in self.students:
            self.students[class_name].append(student)
        else:
            self.students[class_name] = [student]

    def pop_student(self, class_name, index):
        return self.students[class_name].pop(index)
