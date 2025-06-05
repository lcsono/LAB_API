from flask import Flask, jsonify
from flask_swagger_ui import get_swaggerui_blueprint
from flask_jwt_extended import JWTManager
from .extensions import db, ma  # <-- agora importa de extensions



app = Flask(__name__)
app.config.from_object('app.config')

from app.routes.routes import routes
app.register_blueprint(routes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1313)

db.init_app(app)
ma.init_app(app)

# Configuração do JWT
app.config['JWT_SECRET_KEY'] = 'your_secret_key'
jwt = JWTManager(app)

# Importa modelos DEPOIS de configurar o app e o db
from .models import itens
from .routes import routes

# Swagger
SWAGGER_URL = '/swagger'
API_DOC_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_DOC_URL)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

