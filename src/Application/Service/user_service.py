from src.Domain.user import UserDomain
from src.Infrastructure.Model.user import User
from src.config.data_base import db 

class UserService:
    @staticmethod
    def create_user(name, cnpj, email, celular, password, code):
        user = User(name=name, cnpj=cnpj, email=email, celular=celular, password=password, code=code)
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
