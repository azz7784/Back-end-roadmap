from services.user_manager import Usermanager
from response import Response
from errors import AppError

class Usercontroller:
    def __init__(self):
        self.manager = Usermanager()

    def create_user(self, request):
        try:
            self.manager.add_user(
                request.data.get("username"),
                request.data.get("email")
            )

            return Response(
                data={"message" : "User created successfully"},
                status=201
            )

        except AppError as e:
            return Response(
                data={
                    "error":{
                        "code": e.code,
                        "message": e.message
                    }
                },
                status= e.status
            )

        except Exception:
            return Response(
                data={
                    "error":{
                        "code": "INTERNAL_ERROR",
                        "message": "internal server error"
                    }
                },
                status=500
            )

    def list_users(self):
        users=self.manager.list_users()
        return Response(
            data=[str(user) for user in users],
            status=200
        )