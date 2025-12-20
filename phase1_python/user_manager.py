class User :
    def __init__(self, username:str , email:str):
        self.username = username
        self.email = email

    def __repr__(self):
        return f"User(username='{self.username}', email = '{self.email}')"
    

class usermanager:
    def __init__(self):
        self.users = []

    def add_user(self , username: str, email: str):
        user = User(username , email)
        self.users.append(user)

            
    def lis_users(self):
        return self.users
    

def main():
    manger = usermanager()
    manger.add_user("ali", "ali@example.com")
    manger.add_user("sare" ,"sare@example.com")

    for user in manger.lis_users():
        print(user)   


if __name__ == "__main__":
    main()