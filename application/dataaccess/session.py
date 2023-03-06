from abc import ABC, abstractmethod


class Session(ABC):
    @abstractmethod
    def add(self, obj):
        pass

    @abstractmethod
    def commit(self):
        pass        

    @abstractmethod
    def close(self):
        pass

