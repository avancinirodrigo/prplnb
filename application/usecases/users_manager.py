from application.entities.user import User
from application.dataaccess.database import Database
from .response import UseCaseResponse, Success, NotFound

class UsersManager:
    def get_user(self, db: Database, username: str) -> UseCaseResponse:
        session = db.create_session()
        user = db.user_repo().get(username, session)
        session.close()
        if user is None:
            return UseCaseResponse(None, NotFound())    
        return UseCaseResponse(user)

