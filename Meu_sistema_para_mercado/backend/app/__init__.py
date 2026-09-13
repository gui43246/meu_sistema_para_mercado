
from flask import Flask
from .routes.rota_produtos import produtos_bp
from .routes.users.Users_bp import users_bp

app = Flask(__name__)
app.register_blueprint(produtos_bp)
app.register_blueprint(users_bp)