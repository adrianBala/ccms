class Assignment():

    def __init__(self, email, name, url=None, grade=None):
        self.email = email
        self.name = name
        self.url = url
        self.grade = grade

    def get_name(self):
        return self.name
