from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from application.dataaccess.session import Session
from application.repository.file_repo import FileRepo
from sqlalchemy_utils import database_exists, create_database, drop_database
from application.dataaccess.database import Database
from application.repository.user_repo import UserRepo
from .sqlalchemy_session import SqlAlchemySession
from .sqlalchemy_base import Base
from .sqlalchemy_orm import File, User


class SqlAlchemyDatabase(Database):
    def connect(self, url: str):
        self._engine = create_engine(url, pool_pre_ping=True)
        self._session = scoped_session(sessionmaker(bind=self._engine))
        self._url = url

    def create_session(self) -> Session:
        return SqlAlchemySession(self._session())

    @property
    def engine(self):
        return self._engine

    def createdb(self, overwrite: bool = False):
        if database_exists(self._url):
            if overwrite:
                drop_database(self._url)
                create_database(self._url)
        else:
            create_database(self._url)

    def exists(self):
        return database_exists(self._url)

    def drop(self):
        drop_database(self._url)

    def create_all_tables(self):
        Base.metadata.create_all(self._engine)

    def create_all(self, overwrite: bool = False):
        self.createdb(overwrite)
        self.create_all_tables()

    def user_repo(self) -> UserRepo:
        return User()

    def file_repo(self) -> FileRepo:
        return File()
