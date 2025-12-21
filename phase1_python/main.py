from services.user_manager import Usermanager

def main():
    manager = Usermanager()

    try:
        manager.add_user("ali" , "ali@example.com")
        manager.add_user("" , "Invalid-email")
    except ValueError as e:
        print(f"Error: {e}")

    for user in manager.list_users():
        print(user)        
     

if __name__ == "__main__":
    main()