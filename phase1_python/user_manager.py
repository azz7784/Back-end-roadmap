class User :
    def __init__(self, username:str , email:str):
        self.username = username
        self.email = email

    def __repr__(self):
        return f"User(username='{self.username}', email = '{self.email}')"
    
class usermanager:
    def __init__(self):
        self.users = []

    def validate_user(self, username: str, email:str):
         if not username:
            raise ValueError("username is required")
        
         if "@" not in email:
            raise ValueError("invalid email")

    def add_user(self , username: str, email: str):
        self.validate_user(username,email)
        
        user = User(username , email)
        self.users.append(user)


    def list_users(self):
        return self.users
    
def main():
    manger = usermanager()

    try:
        manger.add_user("ali" , "ali@example.com")
        manger.add_user("" ,"invalid email")
    except ValueError as e:
        print(f"Error: {e}")

    for user in manger.list_users():
        print(user)  


if __name__ == "__main__":
    main()