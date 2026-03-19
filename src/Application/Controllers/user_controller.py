import random

from flask import request, jsonify, make_response
from src.Application.Service.user_service import UserService

class UserController:
    @staticmethod
    def register_user():
        try:
            data = request.get_json()

            name = data.get('nome')
            cnpj = data.get('cnpj')
            email = data.get('email')
            celular = data.get('celular')
            password = data.get('senha')

            if not name or not email or not password:
                return make_response(jsonify({"erro": "Missing required fields"}), 400)

            code = str(random.randint(1000, 9999))
            print(f'Código de ativação gerado: {code}')

            user = UserService.create_user(name, cnpj, email, celular, password, code)

            return make_response(jsonify({
                "mensagem": "User salvo com sucesso",
                "usuarios": user.to_dict()
            }), 201)
        except Exception as e:
            print(f"Error registering user: {e}")
            return make_response(jsonify({"erro": f"An error occurred: {e}"}), 500)
    @staticmethod
    def activate_user():
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