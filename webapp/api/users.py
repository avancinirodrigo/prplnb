from flask import jsonify, request
from webapp.controllers.signup_controller import SignUpController
from ..api import bp
from ..api.database import db

@bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json() or {}
    print(data['username'])
    print(data['password'])
    print(type(data))
    print(data)

	# ctrler = UserController()
	# response = ctrler.create(data)
	# return RESTResponse(response).proccess('.get_user')
    # username = data['username']
    # password = data['password']
    ctrl = SignUpController(db, data)

    response = jsonify(data)
    response.status_code = 200
    return response