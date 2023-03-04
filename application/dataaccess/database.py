from abc import ABC, abstractmethod
from application.entities.user import User


class Database(ABC):
	@abstractmethod
	def connect(self, url: str):
		pass

	@abstractmethod
	def user_repo(self, username: str) -> User:
		pass
