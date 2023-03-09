import pytest
from application.usecases.database_manager import DatabaseManager
from application.thirdparties.sqlalchemy.sqlalchemy_database import SqlAlchemyDatabase
from tests.integration.usecases.datastorefs import DatastoreFs


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
    ds = DatastoreFs()
    yield ds
    ds.delete()