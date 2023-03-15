from application.dataaccess.database import Database
from application.usecases.signup import SignUpData, SignUp
from application.usecases.response import Response, MissedInfo


class SignUpController:
    def __init__(self, db: Database, userdata: dict):
        self.db = db
        self.userdata = userdata

    def execute(self) -> Response:
        if ('username' not in self.userdata
                or 'password' not in self.userdata):
            return MissedInfo("SigUp missed some key-value")
        username = self.userdata['username']
        password = self.userdata['password']
        signup_data = SignUpData(username, password)
        uc = SignUp(signup_data)
        return uc.execute(self.db)
