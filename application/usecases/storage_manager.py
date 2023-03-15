from application.dataaccess.database import Database
from application.dataaccess.datastore import Datastore
from application.entities.file import File
from application.usecases.users_manager import UsersManager
from application.usecases.response import NotFound, Success, UseCaseResponse


class StorageManager:
    def __init__(self, db: Database, ds: Datastore):
        self.db = db
        self.ds = ds

    def add_file(self, userdata: dict, file_bytes, desired_url: str):
        users = UsersManager()
        out = users.get_user(self.db, userdata)
        if isinstance(out.response_type, Success):
            user = out.data

            file_repo = self.db.file_repo()
            session = self.db.create_session()
            file = file_repo.get(session, user, desired_url)
            if file is None:
                file = File(desired_url, 0)
                file_repo.add(user, file)
                session.add(file_repo)
            else:
                file.revision = file.revision + 1

            self.ds.add_file(file_bytes, f'{user.username}/{file.revision}{desired_url}')

            session.commit()
            session.close()
            return UseCaseResponse(user)
        return UseCaseResponse(None, NotFound("User not found"))

    def get_file(self, userdata: dict, file_url: str, revision: int = -1):
        users = UsersManager()
        out = users.get_user(self.db, userdata)
        if isinstance(out.response_type, Success):
            user = out.data
            file_repo = self.db.file_repo()
            session = self.db.create_session()
            file = file_repo.get(session, user, file_url)
            session.close()
            if file is not None:
                if revision == -1:  # TODO: revision could have a date
                    revision = file.revision
                file_bytes = self.ds.load_file(f'{user.username}/{revision}{file_url}')
                return UseCaseResponse({
                    'file_bytes': file_bytes,
                    'file': File(file_url, revision)},
                    Success()
                )
            else:
                return UseCaseResponse(None, NotFound("File not found"))
        return UseCaseResponse(None, NotFound("User not found"))
