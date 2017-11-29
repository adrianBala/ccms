class Assignment():

    def __init__(self, email, name, url=None, grade=None):
        self.email = email
        self.name = name
        self.url = url
        self.grade = grade

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_url(self):
        return self.url

    def get_grade(self):
        return self.grade
