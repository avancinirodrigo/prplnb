from application.entities.user import User
from application.dataaccess.database import Database
from .users_manager import UsersManager
from .response import (
    UseCaseResponse,
    Duplicated,
    Success,
    MissedInfo,
    Created
)


class SignUpData:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def to_dict(self):
        return {"username": self.username, "password": self.password}


class SignUp:
    def __init__(self, signup_data: SignUpData):
        self._signup_data = signup_data

    def execute(self, db: Database):
        if (len(self._signup_data.username) == 0
                or len(self._signup_data.password) == 0):
            return UseCaseResponse(None, MissedInfo())
        user = User(self._signup_data.username, self._signup_data.password)
        user_repo = db.user_repo()
        usersman = UsersManager()
        out = usersman.get_user(db, self._signup_data.to_dict())
        if isinstance(out.response_type, Success):
            return UseCaseResponse(None, Duplicated("User already exists"))
        user_repo.add(user)
        session = db.create_session()
        session.add(user_repo)
        session.commit()
        session.close()
        return UseCaseResponse(user_repo, Created())
