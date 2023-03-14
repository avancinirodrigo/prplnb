import os
import pytest
from application.thirdparties.sqlalchemy.sqlalchemy_database import SqlAlchemyDatabase
from application.fs.datastorefs import DatastoreFs


@pytest.fixture(autouse=True)
def db():
    url = 'postgresql://postgres:postgres@localhost:5432/prplndb'
    db = SqlAlchemyDatabase()
    db.connect(url)
    db.create_all(overwrite=True)
    yield db
    db.drop()


@pytest.fixture(autouse=True)
def dsfs():
    ds = DatastoreFs(os.path.dirname(__file__))
    yield ds
    ds.delete()
