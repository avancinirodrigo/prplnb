from abc import ABC, abstractmethod
from application.entities.user import User

class UserRepo:
    # def __init__(self, username: str, password: str):
    #     pass

    @abstractmethod
    def add(self, user: User):
        pass

    @abstractmethod
    def get(self, username: str) -> User:
        pass      
    