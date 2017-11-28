import csv


class UserBaseDao():
    login_file = 'login.csv'

    def import_login_info(self):
        with open(self.login_file, 'r') as csvfile:
            reader = csv.reader(csvfile)
            login_info = []
            for row in reader:
                login_info.append(row)
            return login_info

    def export_login_info(self, login_info):
        with open(self.login_file, 'w') as csvfile:
            writer = csv.writer(csvfile)
            for row in login_info:
                writer.writerow(row)
