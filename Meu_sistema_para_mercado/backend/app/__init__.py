
from flask import Flask
from app.routes.rota_produtos import produtos_bp

app = Flask(__name__)
app.register_blueprint(produtos_bp)