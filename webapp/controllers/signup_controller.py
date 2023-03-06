from application.dataaccess.database import Database
from application.usecases.signup import SignUpData, SignUp
from application.usecases.response import Success
from .response import Response, Created, BadRequest


class SignUpController:
    def __init__(self, db: Database, userdata: dict):
        self.db = db
        self.userdata = userdata

    def execute(self) -> Response:
        if ('username' not in self.userdata
                or 'password' not in self.userdata):
            return BadRequest("SigUp missed field")
        username = self.userdata['username']
        password = self.userdata['password']
        signup_data = SignUpData(username, password)
        uc = SignUp(signup_data)
        out = uc.execute(self.db)
        if isinstance(out.response, Success):
            return Created()