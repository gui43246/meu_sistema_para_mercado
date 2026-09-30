from flask import Flask, render_template
from .routes.rota_produtos import produtos_bp
from .routes.users.Users_bp import users_bp

app = Flask(
    __name__,
    static_folder="../../frontend/css",      # pasta de CSS/JS
    template_folder="../../frontend/pages"     # pasta onde está o index.html
    
)

app.register_blueprint(produtos_bp)
app.register_blueprint(users_bp)


@app.route("/")
def home():
    return render_template("login.html")
