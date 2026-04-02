import time
from flask import Flask
from src.config.data_base import init_db
from src.routes import init_routes
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)
    init_db(app)
    init_routes(app)
    return app

<<<<<<< HEAD
def start_app_with_retry():
    retries = 10
    while retries > 0:
        try:
            print(f"Tentando conectar ao MySQL com SQLAlchemy... ({11 - retries}/10)")
            app = create_app()
            
            print("Conectado com sucesso e aplicação inicializada!")
            return app
        except Exception as e:
            retries -= 1
            print(f"Banco ainda não pronto. Aguardando... Erro: {e}")
            time.sleep(3)
    return None

# NADA de 'app = create_app()' aqui solto!
=======
app = create_app()
>>>>>>> dev

if __name__ == '__main__':
    app.run(debug=True)