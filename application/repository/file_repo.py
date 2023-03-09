from abc import ABC, abstractmethod
from application.entities.file import File
from application.entities.user import User
from application.dataaccess.session import Session

class FileRepo(ABC):

    @abstractmethod
    def add(self, user: User, file: File, revision: int=0):
        pass    

    @abstractmethod
    def get(self, session: Session, user: User, 
            file_url: str, revision: int) -> File:
        pass  