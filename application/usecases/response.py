class Response:
    pass

class Success(Response):
    pass

class Fail(Response):
    pass

class NotFound(Response):
    pass

class Duplicated(Fail):
    pass


class UseCaseResponse:
    def __init__(self, data, response: Response=Success()):
        self.data = data
        self.response = response