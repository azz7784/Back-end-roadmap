from request import Request
from services.user_controller import Usercontroller
def main():
    controller = Usercontroller()
    

    # Create user request
    request = Request({
        "username": "ali",
        "email": "ali@example.com"
    })

    response = controller.create_user(request)
    print(response)

    
    # Invalid user
    bad_request = Request({
        "username": "",
        "email": "invalid"
    })

    print(controller.create_user(bad_request))

    
    # List users
    print(controller.list_users())

     

if __name__ == "__main__":
    main()