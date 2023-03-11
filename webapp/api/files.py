from application.usecases.storage_manager import StorageManager
from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from . import bp
from .dataaccess import db, ds
from .rest_response import RestResponse

@bp.route('/files', methods=['POST'])
@jwt_required()
def add_file():
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