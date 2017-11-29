class AssignmentContainer():

    def __init__(self):
        self.assignments = []

    def get_assignment(self, index):
        return self.assignments[index]

    def add_assignment(self, assignment):
        self.assignments.append(assignment)
