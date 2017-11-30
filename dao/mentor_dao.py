import csv
from model.mentor_model import Mentor


class MentorDao():

    mentors_file = 'mentors.csv'

    def create_mentor(self, name, surname, email, phone, password):
        return Mentor(name, surname, email, phone, password)

    def import_mentors(self):
        mentors = []
        with open(self.mentors_file, "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                mentor = self.create_mentor(*row)
                mentors.append(mentor)
        return mentors

    def export_mentors(self, mentors):
        with open(self.mentors_file, "w") as csvfile:
            writer = csv.writer(csvfile)
            for mentor in mentors:
                writer.writerow(mentor.get_all_details())
