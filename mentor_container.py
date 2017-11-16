class MentorContainer():

    def __init__(self):
        self.mentors = []

    def get_mentors(self):
        return self.mentors

    def add_mentor(self, mentor):
        self.mentors.append(mentor)
