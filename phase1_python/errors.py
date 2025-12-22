class AppError(Exception):
    def __init__(self, code: str, message: str, status: int):
        self.code = code
        self.message = message
        self.status = status
        super().__init__(message)


class ValidationError(Exception):
    def __init__(self , code, message):
        super().__init__(code, message, 400)

class BusinessError(Exception):
    def __init__(self, code, message):
        super().__init__(code, message, 409)