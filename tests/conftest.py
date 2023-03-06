import pytest
from application.usecases.database_manager import DatabaseManager
from application.thirdparties.sqlalchemy.sqlalchemy_database import SqlAlchemyDatabase


@pytest.fixture
def use_db():
    url = 'postgresql://postgres:postgres@localhost:5432/prplndb'
    DatabaseManager.instance().set_db(SqlAlchemyDatabase())
    db = DatabaseManager.instance().db()
    db.connect(url)
    db.create_all(overwrite=True)
    yield
    db.drop()