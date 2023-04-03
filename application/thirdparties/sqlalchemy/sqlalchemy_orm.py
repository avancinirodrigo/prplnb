from sqlalchemy import Column, String, Integer, ForeignKey, and_
from sqlalchemy.orm import relationship
from application.repository.file_repo import FileRepo
from application.repository.user_repo import UserRepo
from application.dataaccess.session import Session
from application.entities.user import User
from application.entities.file import File
from .sqlalchemy_base import Base


class UserRepoMetaclass(type(Base), type(UserRepo)):
    pass


class FileRepoMetaclass(type(Base), type(FileRepo)):
    pass


class User(Base, UserRepo, metaclass=UserRepoMetaclass):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    files = relationship('File', back_populates='user')

    def add(self, user: User):
        self.username = user.username
        self.password = user.password

    def get(self, username: str, session: Session) -> User:
        return session.query(User).filter(User.username == username).first()


class File(Base, FileRepo, metaclass=FileRepoMetaclass):
    __tablename__ = 'files'
    id = Column(Integer, primary_key=True)
    url = Column(String, nullable=False, unique=True)
    revision = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='files')

    def add(self, user: User, file: File):
        self.user = user
        self.url = file.url
        self.revision = file.revision

    def get(self, session: Session, user: User, file_url: str) -> File:
        return session.query(File).filter(and_(User.id == user.id, File.url == file_url)).first()
