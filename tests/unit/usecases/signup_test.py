from application.usecases.signup import SignUpData, SignUp
from application.usecases.users_manager import UsersManager
from application.usecases.database_manager import DatabaseManager
from .user_repo_fake import UserRepoFake
from .database_fake import DatabaseFake

def test_signup():
    url = ''
    DatabaseManager.instance().set_db(DatabaseFake())
    db = DatabaseManager.instance().db()
    db.connect(url)
    db.create_all(overwrite=True)
    user_data = SignUpData("avancinirodrigo@gmail.com", "avancini")
    uc = SignUp(user_data)
    uc.execute(db)
    usersman = UsersManager()
    user = usersman.get_user(user_data.username, db)
    assert user.username == user_data.username 
    assert user.password == user_data.password
    db.drop()