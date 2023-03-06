from application.entities.user import User
from application.dataaccess.database import Database
# from application.

class UsersManager:
    def get_user(self, username: str, db: Database) -> User:
        session = db.create_session()
        user = db.user_repo().get(username, session)
        session.close()
        return user

