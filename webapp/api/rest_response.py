from flask import jsonify
from flask.wrappers import Response
from webapp.controllers.response import Created, BadRequest

class RestResponse:
    @staticmethod    
    def Json(response: Response) -> Response:
        resp = None
        if isinstance(response, Created):
            resp = Response() 
            resp.status_code = 201
        elif isinstance(response, BadRequest):
            resp = jsonify({'message': response.message})
            resp.status_code = 400
        return resp
