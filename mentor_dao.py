import csv
from mentor_model import Mentor

class MentorDao():

    mentors_file = 'mentors.csv'

    def create_mentor(self, name, surname, email, phone, password):
        mentor = MentorModel(name, surname, email, phone, password)
        return mentor

    def import_mentors(self):
        mentors = []
        with open(self.mentors_file, "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                mentor = create_mentor(*row)
                mentors.append(mentor)
        return mentors

    def export_mentors(self, mentors):
        with open(self.mentors_file, "w") as csvfile:
            writer = csv.writer(csvfile)
            for mentor in mentors:
                name = mentor.get_name()
                surname = mentor.get_surname()
                email = mentor.get_email()
                phone = mentor.get_phone_number()
                password = mentor.get_password()
                writer.writerow([name, surname, email, phone, password])
