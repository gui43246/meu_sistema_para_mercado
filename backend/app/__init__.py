from flask import Flask

from backend.app.routes import estoque
app = Flask(__name__)
from app.routes import cadastrar

