import csv


class UserBaseDao():
    login_file = 'login.csv'

    def import_login_info(self):
        with open(self.login_file, 'r') as csvfile:
            reader = csv.reader(csvfile)
            login_info = []
            for row in reader:
                uid, login, password = row
                login_info.append(row)
            return login_info
