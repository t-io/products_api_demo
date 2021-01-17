from flask import request, jsonify
from flask_restful import Resource

from exceptions import APIException
from repositories import ProductRepository


class Product(Resource):
    def get(self, slug: str):
        """ retrieve existing product """
        product = ProductRepository.get(slug)
        return product, 200


class ProductList(Resource):
    def post(self):
        """ create new product """
        request_json = request.get_json(silent=True)
        name: str = request_json['name']
        description: str = request_json['description']
        category: str = request_json['category']
        try:
            product_create = ProductRepository()
            product = product_create.create(name, description, category)
            return product, 201
        except APIException as e:
            response = jsonify(e.to_dict())
            response.status_code = e.status_code
            return response
