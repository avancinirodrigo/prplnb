from flask import jsonify, request
from webapp.controllers.signup_controller import SignUpController
from . import bp
from .database import db

@bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json() or {}
    ctrl = SignUpController(db, data)
    response = jsonify(data)
    response.status_code = 200
    return response