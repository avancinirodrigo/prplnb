import os
import shutil
from io import BytesIO
from application.dataaccess.datastore import Datastore
from application.entities.file import File


class DatastoreFs(Datastore):

    def __init__(self, path: str):
        self.root = f'{path}/datastore'

    def add_file(self, file_bytes: BytesIO, desired_url: str):
        file_dest = f'{self.root}/{desired_url}'
        dir_dest = os.path.dirname(file_dest)
        if not os.path.isdir(dir_dest):
            os.makedirs(dir_dest)
        with open(file_dest, 'wb') as out:
            out.write(file_bytes.read())

    def delete(self):
        if os.path.isdir(self.root):
            shutil.rmtree(self.root)

    def load_file(self, url: str):
        filepath = f'{self.root}/{url}'
        return open(filepath, 'rb')
        # file = open(filepath, 'rb')
        # file_bytes = BytesIO(file)
        # file.close()
        # return file_bytes

    def delete_file(self, filepath):
        pass    

    def list_files(self, directory_name):
        pass               