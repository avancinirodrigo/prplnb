from application.usecases.signup import SignUpData, SignUp
from application.usecases.users_manager import UsersManager
from application.usecases.database_manager import DatabaseManager
from application.usecases.response import UseCaseResponse, Success
from .user_repo_fake import UserRepoFake
from .database_fake import DatabaseFake

def test_signup():
    url = ''
    db = DatabaseFake()
    db.connect(url)
    db.create_all(overwrite=True)
    user_data = SignUpData("avancinirodrigo@gmail.com", "avancini")
    uc = SignUp(user_data)
    uc.execute(db)
    usersman = UsersManager()
    resp = usersman.get_user(db, user_data.to_dict())
    user = resp.data
    assert user.username == user_data.username 
    assert user.password == user_data.password
    db.drop()