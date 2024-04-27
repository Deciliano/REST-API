#! /usr/bin/env python3
from flask import Flask, jsonify, request
from service import ProductService
import logging

app = Flask(__name__)
product_service = ProductService()

@app.route('/products', methods=['GET'])
def get_products():
    products = product_service.get_all_products()
    products_all = [product.__dict__() for product in products]
    return jsonify(products_all)

@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    product = product_service.get_product(id)
    product_one = product.__dict__()
    return jsonify(product_one)

@app.route('/products', methods=['POST'])
def add_product():
    product_data = request.get_json()
    new_product = product_service.add_product(product_data)
    return jsonify(new_product), 201
    
@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    product_data = request.get_json()
    update_product = product_service.update_product(id, product_data)
    return jsonify(update_product)

@app.route('/product/<int:id>', methods=['DELETE'])
def delete_product(id):
    product_service.delete_product(id)
    return jsonify(
        {
            'message': 'Product deleted successfully'
        }
    ), 204

if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)