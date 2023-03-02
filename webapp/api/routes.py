
from flask import jsonify, request
from . import bp as app

from application.usecases import SortService

@app.route('/sort', methods=['POST'])
def sort():
    data = request.json or {}
    sortKeys = data['sortKeys']
    dicts = data['payload']
    ss = SortService(sortKeys, dicts)
    resp = ss.exec()
    response = jsonify(resp)
    response.status_code = 200
    return response