class Assignment():

    def __init__(self, email, name, url='', grade=''):
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

    def get_all_details(self):
        return [self.email, self.name, self.url, self.grade]

    def set_url(self, url):
        self.url = url

    def set_grade(self, grade):
        self.grade = grade

    def set_email(self, email):
        self.email = email
