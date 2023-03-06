class Response:
    pass

class Created(Response):
    pass

class BadRequest:
    def __init__(self, message: str):
        self.message = message