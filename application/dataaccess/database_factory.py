from abc import ABC, abstractmethod
from application.repository.user_repo import UserRepo

class DatabaseFactory(ABC):
    
    @staticmethod
    @abstractmethod
    def user_repo() -> UserRepo:
        pass