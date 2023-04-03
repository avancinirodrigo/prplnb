from application.dataaccess.session import Session


class SessionFake(Session):
    def add(self, obj):
        pass

    def commit(self):
        pass

    def close(self):
        pass
