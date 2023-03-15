from application.usecases.storage_manager import StorageManager
from flask import request
from flask_jwt_extended import jwt_required, get_jwt
from . import bp
from .dataaccess import db, ds
from .rest_response import RestResponse


@bp.route('/files/upload', methods=['POST'])
@jwt_required()
def add_file():
    print(request.__dict__)
    form = request.form.to_dict() or {}
    files = request.files.to_dict() or {}
    userdata = get_jwt()
    print(form)
    print(files)
    file = files['file']
    desired_url = form['desired_url']
    uc = StorageManager(db, ds)
    out = uc.add_file(userdata, file, desired_url)
    return RestResponse.Json(out)


@bp.route('/files/download', methods=['POST'])
@jwt_required()
def get_file():
    form = request.form.to_dict() or {}
    userdata = get_jwt()
    print(form)
    file_url = form['file_url']
    revision = form['revision'] if 'revision' in form else -1
    uc = StorageManager(db, ds)
    out = uc.get_file(userdata, file_url, revision)
    return RestResponse.SendFile(out)
