from application.dataaccess.database import Database
from application.usecases.response import Response, MissedInfo
from application.usecases.create_acccess_token import TokenData, CreateAccessToken
from application.usecases.token_creator import TokenCreator


class TokensController:
    def __init__(self, db: Database, token_creator: TokenCreator, userdata: dict):
        self.db = db
        self.token_creator = token_creator
        self.userdata = userdata

    def execute(self) -> Response:
        if ('username' not in self.userdata
                or 'password' not in self.userdata):
            return MissedInfo("SigUp missed some key-value")
        username = self.userdata['username']
        password = self.userdata['password']
        token_data = TokenData(username, password, self.token_creator)
        uc = CreateAccessToken(self.db, token_data)
        return uc.execute()
