from src.Domain.product import ProductDomain
from src.Infrastructure.Model.product import Product
from src.config.data_base import db
# from datetime import datetime, timedelta
# import jwt
# import os 

class ProductService:
    def get_all_products():
        products = db.session.query(Product).all()
        return [ProductDomain(product.id, product.name, product.price, product.quantity, product.status, product.image)for product in products]
    
    @staticmethod
    def create_product(name, price, quantity, image):
        # 1. Valida se já existe
        if db.session.query(Product).filter(Product.name == name).first():
            return {"success": False, "message": "Já há um produto cadastrado com esse nome!"}
        
        # 2. Se não existe, cria o produto
        product = Product(name=name, price=price, quantity=quantity, image=image)
        db.session.add(product)
        db.session.commit()
 
        # 3. Monta o objeto de domínio
        product = ProductDomain(
            product.id, product.name, product.price, 
            product.quantity, product.status, product.image
        )

        # 4. Retorna sucesso com o objeto
        return {
            "success": True,
            "produto": product
        }
    
    def update_product(product_id, data):
        product = db.session.query(Product).filter(Product.id == product_id).first()
        if not product:
            return {"success": False, "message": "Produto não encontrado!"}
        
        if 'name' in data:
            product.name = data['name']
        if 'image' in data:
            product.image = data['image']
        if 'price' in data:
            product.price = data['price']
        if 'quantity' in data:
            product.quantity = data['quantity']
        if 'status' in data:
            product.status = data['status']

        try:
            db.session.commit()
            return {"success": True, "message": "Informações do produto atualizadas com sucesso."}
        except Exception as e:
            db.session.rollback()
            return {"success": False, "message": f"Erro ao atualizar o banco de dados: {str(e)}"}
