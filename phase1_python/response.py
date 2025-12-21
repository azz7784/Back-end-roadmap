class Response:
    def __init__(self, data=None, status=200):
        self.data = data
        self.status = status


    def __repr__(self):
        return f"Response(status={self.status}, data = {self.data})"