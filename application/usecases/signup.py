from application.repository.user_repo import UserRepo
from application.entities.user import User
from application.dataaccess.database import Database
from .users_manager import UsersManager
from .response import UseCaseResponse, Duplicated, Success

class SignUpData:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

class SignUp:
    def __init__(self, signup_data: SignUpData):
        self._signup_data = signup_data

    def execute(self, db: Database):
        user = User(self._signup_data.username, self._signup_data.password)
        user_repo = db.user_repo()
        usersman = UsersManager()
        out = usersman.get_user(db, self._signup_data.username)
        if isinstance(out.response, Success):
            return (out.data, Duplicated())        
        user_repo.add(user)
        session = db.create_session()
        session.add(user_repo)
        session.commit()
        return UseCaseResponse(user_repo, Success())
        
