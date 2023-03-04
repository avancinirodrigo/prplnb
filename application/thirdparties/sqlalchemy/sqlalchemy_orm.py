from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property
from application.repository.user_repo import UserRepo
from application.entities.user import User as UserEntity
from application.dataaccess.session import Session
from application.entities.user import User
from .sqlalchemy_base import Base


class User(Base, UserRepo):
    __tablename__ = 'users'	
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

    # def __init__(self, user: UserEntity):
	# 	# user = User(name, password)
    #     self.username = username
    #     self.password = password
	# 	self.session

	# def begin(self):
    def get_user(self, username: str, session: Session) -> User:
        return session.query(User).filter(User.username == username).one()
