from abc import ABC, abstractmethod


class Session(ABC):
	@abstractmethod
	def add(self, url: str):
		pass

	@abstractmethod
	def commit(self):
		pass        