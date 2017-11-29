import csv

from assignment_model import Assignment


class AssignmentDao():
    assignments_file = 'assignments.csv'

    def create_assignment(self, email, name, url='', grade=''):
        return Assignment(email, name, url, grade)

    def import_assignments(self):
        assignments = []
        with open(self.assignments_file, "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                assignment = self.create_assignment(*row)
                assignments.append(assignment)
        return assignments

    def export_assignments(self, assignments):
        with open(self.assignments_file, "w") as csvfile:
            writer = csv.writer(csvfile)
            for assignment in assignments:
                writer.writerow(assignment.get_all_details())

    def get_student_assignments(self, email):
        assignments = self.import_assignments()
        student_assignments = []
        for assignment in assignments:
            if assignment.get_email() == email:
                student_assignments.append(assignment)
        return student_assignments
