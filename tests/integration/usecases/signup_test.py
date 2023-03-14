from application.usecases.signup import SignUpData, SignUp
from application.usecases.users_manager import UsersManager
from application.usecases.response import Success, Created, Duplicated


def test_happy_path(db):
    user_data = SignUpData("avancinirodrigo@gmail.com", "avancini")
    uc = SignUp(user_data)
    uc.execute(db)
    usersman = UsersManager()
    resp = usersman.get_user(db, user_data.to_dict())
    user = resp.data
    assert isinstance(resp.response_type, Success)
    assert user.username == user_data.username
    assert user.password == user_data.password


def test_username_exists(db):
    user_data1 = SignUpData("avancinirodrigo@gmail.com", "avancini")
    uc = SignUp(user_data1)
    r1 = uc.execute(db)
    assert isinstance(r1.response_type, Created)

    user_data2 = SignUpData("avancinirodrigo@gmail.com", "avancini")
    uc = SignUp(user_data2)
    r2 = uc.execute(db)
    assert isinstance(r2.response_type, Duplicated)
