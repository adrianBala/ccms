class AssignmentContainer():

    def __init__(self):
        self.assignments = []

    def get_assignments(self):
        return self.assignments

    def get_assignments_of_student(self, email):
        assignments_of_student = []
        for assignment in self.assignments:
            if assignment.get_email() == email:
                assignments_of_student.append(assignment)

        return assignments_of_student

    def set_assignments(self, assignments):
        self.assignments = assignments

    def add_assignment(self, assignment):
        self.assignments.append(assignment)

    def remove_assignments(self, email):
        for assignment in self.assignments:
            if assignment.get_email() == email:
                self.assignments.remove(assignment)

    def change_email(self, old_email, new_email):
        for assignment in self.get_assignments():
            if assignment.get_email() == old_email:
                assignment.set_email(new_email)
