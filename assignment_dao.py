import csv

from assignment_model import Assignment


class AssignmentDao():
    assignment_file = 'assignments.csv'

    def create_assignment(self, email, name, url='', grade=''):
        return Assignment(email, name, url, grade)

    def import_assignments(self):
        assignments = []
        with open(self.assignment_file, "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                print(row)
                assignment = self.create_assignment(*row)
                assignments.append(assignment)
        return assignments
