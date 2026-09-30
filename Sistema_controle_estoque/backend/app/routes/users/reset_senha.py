from .Users_bp import users_bp
from app.DATABASE import get_db
from flask import request,jsonify

@users_bp.route("/reset_senha",methods=["POST"])
def resetar_senha():
    requisição=request.get_json(silent=True)
    campos_obrigratorios=['DRT','nova_senha','comfirmar_senha']
    if not isinstance(dict,requisição)or any(campo not in requisição for campo in campos_obrigratorios):
        return jsonify({"mensagem":"sem resultado,verifique os campos"}),404
    drt=requisição["DRT"]
    nova_senha=requisição["nova_senha"]
    confirmar_senha=requisição['confirmar_senha']
    