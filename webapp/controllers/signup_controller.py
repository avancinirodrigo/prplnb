from application.dataaccess.database import Database
from application.usecases.signup import SignUpData, SignUp


class SignUpController:
    def __init__(self, db: Database, userdata: dict):
        username = userdata['username']
        password = userdata['password']
        signup_data = SignUpData(username, password)
        uc = SignUp(signup_data)
        uc.execute(db)