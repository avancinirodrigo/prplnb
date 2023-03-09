class Response:
    pass

class Success(Response):
    pass

class Created(Success):
    pass

class Failure(Response):
    def __init__(self, message: str):
        self.message = message

class NotFound(Failure):
    pass

class Duplicated(Failure):
    pass

class MissedInfo(Failure):
    pass

class NotMatched(Failure):
    pass

class UseCaseResponse:
    def __init__(self, data, response_type: Response=Success()):
        self.data = data
        self.response_type = response_type