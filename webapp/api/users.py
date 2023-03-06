from flask import jsonify, request
from webapp.controllers.signup_controller import SignUpController
from . import bp
from .database import db
from .rest_response import RestResponse

@bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json() or {}
    ctrl = SignUpController(db, data)
    return RestResponse.Json(ctrl.execute())