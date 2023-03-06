from application.usecases.database_manager import DatabaseManager
from webapp.controllers.signup_controller import SignUpController
from webapp.controllers.response import Created


def test_signup(use_db):
    db = DatabaseManager.instance().db()
    userdata = {'username': 'avancinirodrigo@gmail.com', 'password': 'avancini'}
    ctrl = SignUpController(db, userdata)
    resp = ctrl.execute()
    assert isinstance(resp, Created)
