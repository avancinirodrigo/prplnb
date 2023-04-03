from application.dataaccess.database import Database
from application.repository.user_repo import UserRepo


class DatabaseManager:
    _instance = None
    _database = None

    def set_db(self, database: Database):
        self._database = database

    def db(self) -> Database:
        return self._database

    def user_repo(self) -> UserRepo:
        return self._dbfactory.user_repo()

    @classmethod
    def Instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
