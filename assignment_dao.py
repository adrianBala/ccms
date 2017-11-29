from assignment_model import Assignment


class AssignmentDao():
    assignment_file = 'assignments.csv'

    def create_assignment(self, email, name, url=None, grade=None):
        return Assignment(email, name, url, grade)
