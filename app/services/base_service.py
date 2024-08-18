from app.common.http_methods import GET, POST, PUT
from flask import Blueprint, Request, jsonify, request

from app.controllers.base import BaseController

class BaseService:

    def create(self, request: Request, controller: BaseController):
        data, error = controller.create(request.json)
        response = data if not error else {'error': error}
        status_code = 200 if not error else 400
        return jsonify(response), status_code
    
    def update(self, request: Request, controller: BaseController):
        data, error = controller.update(request.json)
        response = data if not error else {'error': error}
        status_code = 200 if not error else 400
        return jsonify(response), status_code

    def delete_by_id(self, _id: int, controller: BaseController):
        data, error = controller.delete(_id)
        response = data if not error else {'error': error}
        status_code = 200 if data else 404 if not error else 400
        return jsonify(response), status_code

    def get_by_id(self, _id: int, controller: BaseController):
        data, error = controller.get_by_id(_id)
        response = data if not error else {'error': error}
        status_code = 200 if data else 404 if not error else 400
        return jsonify(response), status_code

    def get_all(self, controller: BaseController):
        data, error = controller.get_all()
        response = data if not error else {'error': error}
        status_code = 200 if data else 404 if not error else 400
        return jsonify(response), status_code
