from services.user_manager import Usermanager
from response import Response

class Usercontroller:
    def __init__(self):
        self.manager = Usermanager()

    def create_user(self, request):
        try:
            username = request.data.get("username")
            email = request.data.get("email")

            self.manager.add_user(username,email)

            return Response(
                data={"massage" : "User created successfully"},
                status=201
            )
        except ValueError as e:
            return Response(
                data={"error": str(e)},
                status= 400
            )
    def list_users(self):
        users=self.manager.list_users()
        return Response(
            data=[str(user) for user in users],
            status=200
        )