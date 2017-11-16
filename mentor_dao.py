import csv
from mentor_model import Mentor

class MentorDao():

    mentors_file = 'mentors.csv'

    def import_mentors(self):
        mentors = []
        with open(self.mentors_file, "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                mentors.append(row)
        return mentors
