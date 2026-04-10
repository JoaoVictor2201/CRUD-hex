import os
from src.Application.Controllers.user_controller import UserController
from src.Application.Controllers.product_controller import ProductController
from flask import jsonify, make_response

# ROTAS DE USER
def init_routes(app):    
    @app.route('/api', methods=['GET'])
    def health():
        return make_response(jsonify({
            "mensagem": "API - OK; Docker - Up",
        }), 200)
    
    @app.route('/users', methods=['GET'])
    def get_all_users():
        return UserController.get_all_users()
    
    @app.route('/user', methods=['POST'])
    def register_user():
        return UserController.register_user()

    @app.route('/user/activate', methods=['POST'])
    def activate_user():
        return UserController.activate_user()

    @app.route('/login', methods=["POST"])
    def login():
        return UserController.login()
    
    @app.route('/user', methods=['PUT'])
    def update_user():
        return UserController.update_user()
    
#ROTAS DE PRODUTO
    @app.route('/product', methods=['GET'])
    def get_all_products():
        return ProductController.get_all_products()
    
    @app.route('/product', methods=['POST'])
    def create_product():
        return ProductController.create_product()