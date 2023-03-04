from application.repository.user_repo import UserRepo
from application.entities.user import User
from application.dataaccess.database import Database
from application.dataaccess.database_factory import DatabaseFactory
from application.usecases.database_manager import DatabaseManager


class SignUpData:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class SignUp:
    def __init__(self, signup_data: SignUpData):
        self._signup_data = signup_data
        print(signup_data.username)

    def execute(self, db: Database):
        # user = User(self._signupData.username, self._signupData.password)
        user_repo = db.user_repo()
        user_repo.username = self._signup_data.username
        user_repo.password = self._signup_data.password
        session = db.create_session()
        session.add(user_repo)
        session.commit()
        
