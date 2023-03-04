from application.repository.user_repo import UserRepo
from application.entities.user import User

class UserRepoFake(UserRepo):
    def __init__(self):
        self.users = {}
    
    def add(self, user: User):
        self.users[user.name] = user

    def get(self, name: str) -> User:
        return self.users[name]

    def commit(self):
        pass