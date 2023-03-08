from flask import jsonify
from flask.wrappers import Response
from application.usecases.response import (
    UseCaseResponse,
    Created,
    MissedInfo,
    Duplicated
)

class RestResponse:
    @staticmethod    
    def Json(response: UseCaseResponse) -> Response:
        resp = None
        if isinstance(response.response_type, Created):
            resp = RestResponse.Created()
        elif isinstance(response.response_type, MissedInfo):
            resp = RestResponse.BadRequest(response.response_type.message)
        elif isinstance(response.response_type, Duplicated):
            resp = RestResponse.Conflict(response.response_type.message)
        return resp

    @staticmethod 
    def Created() -> Response:
        resp = Response() 
        resp.status_code = 201
        return resp

    @staticmethod 
    def BadRequest(message: str) -> Response:
        resp = jsonify({'message': message})
        resp.status_code = 400
        return resp

    @staticmethod 
    def Conflict(message: str) -> Response:
        resp = jsonify({'message': message})
        resp.status_code = 409
        return resp        
