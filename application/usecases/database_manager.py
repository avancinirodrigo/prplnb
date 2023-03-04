from application.dataaccess.database import Database
from application.dataaccess.database_factory import DatabaseFactory
from application.repository.user_repo import UserRepo


class DatabaseManager:
    _instance = None
    
    # def __init__(self, database: Database, dbfactory: DatabaseFactory):
    #     self._database = database
    #     self._dbfactory = dbfactory

    def set_database(self, database: Database):
        self._database = database

    def set_dbfactory(self, dbfactory: DatabaseFactory):
        self._dbfactory = dbfactory

    def db(self) -> Database:
        return self._database

    def user_repo(self) -> UserRepo:
        return self._dbfactory.user_repo()

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance