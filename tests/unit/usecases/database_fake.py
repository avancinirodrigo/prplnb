from application.dataaccess.database import Database
from application.dataaccess.session import Session
from application.entities.user import User
from .user_repo_fake import UserRepoFake
from .session_fake import SessionFake


class DatabaseFake(Database):
    def connect(self, url: str):
        pass

    def user_repo(self) -> User:
        return UserRepoFake()

    def create_all(self, overwrite: bool):
        pass

    def create_session(self) -> Session:
        return SessionFake()

    def drop(self):
        pass