import os


class TestsHelper:
    @staticmethod
    def GetDataDirPath() -> str:
        return f'{os.path.dirname(__file__)}/data'