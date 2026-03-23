import code
import jwt
import os
from flask import request, jsonify, make_response
from src.Application.Service.user_service import UserService
from src.Infrastructure.http.whats_app import WhatsAppService

SECRET_KEY = os.getenv("SECRET_KEY", "sua-chave-super-secreta")

class UserController:
    @staticmethod
    def register_user():
        data = request.get_json()

        name = data.get('nome')
        cnpj = data.get('cnpj')
        email = data.get('email')
        celular = data.get('celular')
        password = data.get('senha')

        if not name or not email or not password:
            return make_response(jsonify({"erro": "Missing required fields"}), 400)

        code = WhatsAppService.generate_code()

        user = UserService.create_user(name, cnpj, email, celular, password, code)
        
        WhatsAppService().send_activation_message(celular, code)

        return make_response(jsonify({
            "mensagem": "User salvo com sucesso",
            "usuarios": user.to_dict()
        }), 201)
    
    @staticmethod
    def activate_user(data=None):
        if data is None:
            data = request.get_json()
        cnpj = data.get('cnpj')
        activation_code = data.get('activation_code')

        if not cnpj or not activation_code:
            return make_response(jsonify({"erro": "CNPJ e código de ativação são obrigatórios"}), 400)

        success = UserService.activate_user(cnpj, activation_code)
        if success:
            return make_response(jsonify({"mensagem": "Conta ativada com sucesso"}), 200)
        else:
            return make_response(jsonify({"erro": "Código de ativação inválido ou vendedor não encontrado"}), 400)

    @staticmethod
    def login(data=None):
        if data is None:
            data = request.get_json()

        cnpj = data.get('cnpj')
        password = data.get('password') 

        if not cnpj or not password:
            return make_response(jsonify({"erro": "CNPJ e senha são obrigatórios"}), 400)

        result = UserService.authenticate_user(cnpj, password)
        
        if result["success"]:
            return make_response(jsonify({
                "mensagem": "Login realizado com sucesso",
                "token": result["token"]
            }), 200)
        else:
            return make_response(jsonify({"erro": result["message"]}), 401)

    @staticmethod
    def get_all_users():
        users = UserService.get_all_users()
        return make_response(jsonify({
            "mensagem": "Usuários encontrados com sucesso",
            "usuarios": [user.to_dict() for user in users]
        }), 200)