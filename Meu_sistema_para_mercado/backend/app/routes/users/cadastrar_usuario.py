from flask import request,jsonify
from .Users_bp import users_dp
from app.DATABASE import get_db

@users_dp.route("/Cadastro_usuario",methods=["POST"])
def cadastrar_usuario():
    dados = request.get_json(silent=True)
    obrigatorio=["DRT","name","Email","numero_tel","senha"]
    
    if not isinstance(dados,dict) or  any(campo not in dados for campo in obrigatorio):
        return jsonify({"mensagem":"sem resultado, verifique os dados"}),404
    
    DRT = dados["DRT"]
    name = dados["name"]
    Email = dados["Email"]
    numero_tel = dados["numero_tel"]
    senha = dados["senha"]
    