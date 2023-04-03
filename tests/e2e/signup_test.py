from application.usecases.response import Created
from webapp.controllers.signup_controller import SignUpController


def test_signup(db):
    userdata = {'username': 'avancinirodrigo@gmail.com', 'password': 'avancini'}
    ctrl = SignUpController(db, userdata)
    resp = ctrl.execute()
    assert isinstance(resp.response_type, Created)
