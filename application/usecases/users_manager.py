from application.dataaccess.database import Database
from .response import UseCaseResponse, NotFound, NotMatched, MissedInfo

class UsersManager:
    def get_user(self, db: Database, userdata: dict) -> UseCaseResponse:
        if ('username' not in userdata
                or 'password' not in userdata):
            return UseCaseResponse(None, MissedInfo("SigUp missed some key-value"))
        session = db.create_session()
        user = db.user_repo().get(userdata['username'], session)
        session.close()
        if user is None:
            return UseCaseResponse(None, NotFound("User not found"))    
        if user.password != userdata['password']:
            return UseCaseResponse(None, NotMatched("Password not matched"))    
        return UseCaseResponse(user)

