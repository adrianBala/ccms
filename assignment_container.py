class AssignmentContainer():

    def __init__(self):
        self.assignments = []

    def get_assignment(self, index):
        return self.assignments[index]

    def set_assignments(self, assignments):
        self.assignments = assignments

    def add_assignment(self, assignment):
        self.assignments.append(assignment)

    def remove_assignments(self, email):
        for assignment in self.assignments:
            if assignment.get_email() == email:
                self.assignments.remove(assignment)
