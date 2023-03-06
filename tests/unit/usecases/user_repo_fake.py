from application.dataaccess.session import Session
from application.repository.user_repo import UserRepo
from application.entities.user import User

users = {}

class UserRepoFake(UserRepo):
    
    def add(self, user: User):
        users[user.username] = user

    def get(self, username: str, session: Session) -> User:
        return users[username] if username in users else None
