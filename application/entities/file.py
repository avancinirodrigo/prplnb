import os


class File:
    def __init__(self, url: str, revision: int):
        self.url = url
        self.path, self.name = os.path.split(url)
        self.revision = revision
