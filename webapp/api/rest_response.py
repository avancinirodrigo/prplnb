from typing import Union
from flask import jsonify, send_file
from flask.wrappers import Response
from application.usecases.response import (
    UseCaseResponse,
    Success,
    Created,
    MissedInfo,
    Duplicated,
    NotFound
)

class RestResponse:
    @staticmethod    
    def Json(response: UseCaseResponse) -> Response:
        if isinstance(response.response_type, Success):
            return RestResponse.Ok()
        if isinstance(response.response_type, Created):
            return RestResponse.Created()
        elif isinstance(response.response_type, MissedInfo):
            return RestResponse.BadRequest(response.response_type.message)
        elif isinstance(response.response_type, Duplicated):
            return RestResponse.Conflict(response.response_type.message)
        elif isinstance(response.response_type, NotFound):
            return RestResponse.NotFound(response.response_type.message)        
        return RestResponse.NotImplemented(f'Response not implemented yet {response.__dict__}')
    
    @staticmethod    
    def SendFile(response: UseCaseResponse) -> Union[Response, None]:
        if isinstance(response.response_type, Success):
            file = response.data['file']
            return send_file(response.data['file_bytes'],
			                 download_name=file.name,
                             as_attachment=True)
        else:
            return RestResponse.Json(response)

    @staticmethod 
    def Ok() -> Response:
        resp = Response() 
        resp.status_code = 200
        return resp

    @staticmethod 
    def Created() -> Response:
        resp = Response() 
        resp.status_code = 201
        return resp

    @staticmethod 
    def Failure(message: str, status: int) -> Response:
        resp = jsonify({'message': message})
        resp.status_code = status
        return resp

    @staticmethod 
    def BadRequest(message: str) -> Response:
        return RestResponse.Failure(message, 400)

    @staticmethod 
    def Conflict(message: str) -> Response:
        return RestResponse.Failure(message, 409)

    @staticmethod 
    def NotImplemented(message: str) -> Response:
        return RestResponse.Failure(message, 501)
    
    @staticmethod 
    def NotFound(message: str) -> Response:
        return RestResponse.Failure(message, 501)    
      
