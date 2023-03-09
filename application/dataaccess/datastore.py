from abc import ABC, abstractmethod


class Datastore(ABC):

    @abstractmethod
    def add_file(self, file, destination):
        pass

    @abstractmethod
    def load_file(self, filepath):
        pass

    @abstractmethod
    def delete_file(self, filepath):
        pass    

    @abstractmethod
    def list_files(self, directory_name):
        pass     

    @abstractmethod
    def delete(self, directory_name):
        pass  