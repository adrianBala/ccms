import csv
from mentor_model import Mentor

class MentorDao():

    mentors_file = 'mentors.csv'

    def create_mentor(self, row):
        name, surname, email, phone, password = row
        mentor = MentorModel(name, surname, email, phone, password)
        return mentor

    def import_mentors(self):
        mentors = []
        with open(self.mentors_file, "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                mentor = create_mentor(row)
                mentors.append(mentor)
        return mentors
