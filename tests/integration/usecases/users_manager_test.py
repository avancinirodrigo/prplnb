from application.usecases.users_manager import UsersManager
from application.usecases.database_manager import DatabaseManager
from application.usecases.response import NotFound


def test_get_user_not_exists(db):
    uc = UsersManager()
    userdata = {"username": "avancinirodrigo", "password": "avancini"}
    resp = uc.get_user(db, userdata)
    assert resp.data is None
    assert isinstance(resp.response_type, NotFound)

