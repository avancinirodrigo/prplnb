from application.usecases.users_manager import UsersManager
from application.usecases.database_manager import DatabaseManager
from application.usecases.response import NotFound


def test_get_user_not_exists(use_db):
    db = DatabaseManager.instance().db()
    uc = UsersManager()
    resp = uc.get_user(db, 'avancinirodrigo')
    assert resp.data is None
    assert isinstance(resp.response, NotFound)

