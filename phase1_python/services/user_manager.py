from models.user import User


class Usermanager:
    def __init__(self):
        self.users = []


    def validate_user (self , username:str , email:str):
        if not username:
            raise ValueError ("Username is required")

        if "@" not in email:
            raise ValueError ("Invalid email") 


    def add_user(self, username:str , email:str):
        self.validate_user(username,email)
        user = User(username,email)
        self.users.append(user)


    def list_users(self):
        return self.users