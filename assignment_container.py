class AssignmentContainer():

    def __init__(self):
        self.assignments = []

    def get_assignment(self, index):
        return self.assignments[index]

    def add_assignment(self, assignment):
        self.assignments.append(assignment)

    def remove_assignments(self, email):
        for assignment in self.assignments:
            if assignment.get_email() == email:
                self.assignments.remove(assignment)
