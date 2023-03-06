from application.usecases.signup import SignUpData, SignUp
from application.usecases.users_manager import UsersManager
from application.usecases.database_manager import DatabaseManager
from application.usecases.response import UseCaseResponse, Success


def test_happy_path(use_db):
    db = DatabaseManager.instance().db()
    user_data = SignUpData("avancinirodrigo@gmail.com", "avancini")
    uc = SignUp(user_data)
    uc.execute(db)
    usersman = UsersManager()
    resp = usersman.get_user(db, user_data.username)
    user = resp.data
    assert isinstance(resp.response, Success)
    assert user.username == user_data.username 
    assert user.password == user_data.password

def test_username_exists(use_db):
    db = DatabaseManager.instance().db()
    user_data1 = SignUpData("avancinirodrigo@gmail.com", "avancini")
    uc = SignUp(user_data1)
    uc.execute(db)

    user_data2 = SignUpData("avancinirodrigo@gmail.com", "avancini")
    uc = SignUp(user_data2)
    uc.execute(db)    