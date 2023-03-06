from application.repository.user_repo import UserRepo
from application.entities.user import User
from application.dataaccess.database import Database


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
        user_repo.add(user)
        session = db.create_session()
        session.add(user_repo)
        session.commit()
        
