class UserBaseView():

    def get_email(self):
        user_email = input('Enter e-mail: ')
        return user_email

    def get_password(self):
        user_password = input('Enter password: ')
        return user_password

    def display_text(self, text):
        print(text)
