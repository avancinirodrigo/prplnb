from flask import request, jsonify
from flask_jwt_extended import create_access_token
from application.usecases.users_manager import UsersManager
from application.usecases.response import UseCaseResponse, Success
from . import bp
from .dataaccess import db
from .rest_response import RestResponse


@bp.route('/tokens', methods=['POST'])
def create_token():
    userdata = request.get_json() or {}
    uc = UsersManager()
    out = uc.get_user(db, userdata)
    print(out.response_type)
    if isinstance(out.response_type, Success):
        user = out.data
        print(user.__dict__)
        access_token = create_access_token(identity=user.id, 
                                           additional_claims=userdata)
        return jsonify({ "token": access_token, "user_id": user.id }), 200
    return RestResponse.Json(out)