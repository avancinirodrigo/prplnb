import os
from application.fs.datastorefs import DatastoreFs
from application.thirdparties.sqlalchemy.sqlalchemy_database import SqlAlchemyDatabase


db = SqlAlchemyDatabase()
ds = DatastoreFs(f'{os.environ.get("HOME")}/prpln')
