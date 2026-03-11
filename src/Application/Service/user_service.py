from src.Domain.user import UserDomain
from src.Infrastructure.Model.user import User
from src.config.data_base import db 

class UserService:
    @staticmethod
    def create_user(name, cnpj, email, celular, password):
        user = User(name=name, cnpj=cnpj, email=email, celular=celular, password=password)        
        db.session.add(user)
        db.session.commit()       
        
        return UserDomain(user.id, user.name, user.cnpj, user.email, user.celular, user.status)