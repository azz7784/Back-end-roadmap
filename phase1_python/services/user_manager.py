from models.user import User
from errors import ValidationError , BusinessError


class Usermanager:
    def __init__(self):
        self.users = []


    def validate_user (self , username:str , email:str):
        if not username:
            raise ValidationError (
                code= "USERNAME_REQUIRED",
                message= "username is required"
            )

        if "@" not in email:
            raise ValidationError (
                code= "INVALID_EMAIL",
                message= "email is invalid"
            ) 


    def add_user(self, username:str , email:str):
        self.validate_user(username,email)

        for user in self.users:
            if user.username == username:
                raise BusinessError(
                    code= "USERNAME_EXISTS",
                    message= "username already exists"
                )

        self.users.append(User(username, email))