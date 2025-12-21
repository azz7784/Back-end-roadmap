class User:
    def __init__(self, username:str , email:str):
        self.username = username
        self.email = email

    def __repr__(self):
        return f"User(username= '{self.username}', email= '{self.email}')"
