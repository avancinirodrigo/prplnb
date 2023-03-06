from abc import ABC, abstractmethod
from application.entities.user import User
from application.dataaccess.session import Session

class UserRepo(ABC):

    @abstractmethod
    def add(self, user: User):
        pass    

    @abstractmethod
    def get(self, username: str, session: Session) -> User:
        pass      
    