class StudentContainer():

    def __init__(self):
        self.students = {}

    def get_students(self):
        return self.students

    def get_all_students(self):
        all_students = []
        for student_list in self.students.values():
            all_students.extend(student_list)
        return all_students

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

    def remove_student(self, student, class_name):
        self.students[class_name].remove(student)
