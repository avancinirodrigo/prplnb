from application.dataaccess.database_factory import DatabaseFactory
from application.repository.user_repo import UserRepo
from .sqlalchemy_orm import User

class SqlAchemyFactory(DatabaseFactory):

    @staticmethod
    def user_repo() -> UserRepo:
        return User()