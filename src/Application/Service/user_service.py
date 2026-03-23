from src.Domain.user import UserDomain
from src.Infrastructure.Model.user import User
from src.config.data_base import db 
from datetime import datetime, timedelta
import jwt
import os  
from werkzeug.security import generate_password_hash, check_password_hash


SECRET_KEY = os.getenv("SECRET_KEY", "sua-chave-super-secreta")

class UserService:
    @staticmethod
    def get_all_users():
        users = db.session.query(User).all()
        return [UserDomain(user.id, user.name, user.cnpj, user.email, user.celular, user.status, user.code) for user in users]
    
    @staticmethod
    def create_user(name, cnpj, email, celular, password, code):
        password_hash = generate_password_hash(password, method="pbkdf2:sha256", salt_length=16)
        user = User(name=name, cnpj=cnpj, email=email, celular=celular, password=password_hash, code=code)
        db.session.add(user)
        db.session.commit()       
        
        return UserDomain(user.id, user.name, user.cnpj, user.email, user.celular, user.status, user.code)
    

    @staticmethod
    def activate_user(cnpj, activation_code):
        user = db.session.query(User).filter(User.cnpj == cnpj, User.code == activation_code).first()
        if user:
            user.status = "Ativo"
            db.session.commit()
            return True
        return False
    
    @staticmethod
    def authenticate_user(cnpj, password):
        user = db.session.query(User).filter(User.cnpj == cnpj).first()
        if not user or not check_password_hash(user.password, password):
            return {"success": False, "message": "Credenciais inválidas. CNPJ ou senha incorretos."}

        if user.status != "Ativo":
            return {"success": False, "message": "Usuário inativo. Por favor, ative sua conta primeiro."}
        
        token = jwt.encode(
            {
                "user_id": user.id, 
                "cnpj": user.cnpj, 
                "exp": datetime.utcnow() + timedelta(hours=1)
            },
            SECRET_KEY,
            algorithm="HS256"
        )
        
        return {"success": True, "token": token}

