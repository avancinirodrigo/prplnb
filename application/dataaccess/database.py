from abc import ABC, abstractmethod
from application.entities.user import User
from .session import Session


class Database(ABC):
    @abstractmethod
    def connect(self, url: str):
        pass

    @abstractmethod
    def create_all(self, overwrite: bool):
        pass

    @abstractmethod
    def create_session(self) -> Session:
        pass

    @abstractmethod
    def drop(self):
        pass

    @abstractmethod
    def user_repo(self, username: str) -> User:
        pass
