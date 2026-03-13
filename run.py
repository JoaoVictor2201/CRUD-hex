import time
from flask import Flask
from src.config.data_base import init_db
from src.routes import init_routes

def create_app():
    app = Flask(__name__)
    init_db(app)
    init_routes(app)
    return app

def start_app_with_retry():
    retries = 10
    while retries > 0:
        try:
            print(f"Tentando conectar ao MySQL com SQLAlchemy... ({11 - retries}/10)")
            app = create_app()
            
            # ATENÇÃO: Se o seu init_db não força a criação das tabelas, 
            # o erro pode só estourar mais tarde. O ideal é que o init_db 
            # já teste a conexão.
            
            print("Conectado com sucesso e aplicação inicializada!")
            return app
        except Exception as e:
            retries -= 1
            print(f"Banco ainda não pronto. Aguardando... Erro: {e}")
            time.sleep(3)
    return None

# NADA de 'app = create_app()' aqui solto!

if __name__ == '__main__':
    app = start_app_with_retry()
    if app:
        app.run(host='0.0.0.0', port=5000, debug=True)
    else:
        print("Falha crítica: Não foi possível conectar ao banco de dados após várias tentativas.")