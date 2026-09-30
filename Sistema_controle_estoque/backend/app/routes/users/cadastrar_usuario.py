from flask import request,jsonify
import sqlite3
from .Users_bp import users_bp
from app.DATABASE import get_db
from app.services.service_pra_users import *
from app.security.hash import criar_hash
@users_bp.route("/Cadastro_usuario", methods=["POST"])
def cadastrar_usuario():
    
    dados = request.get_json(silent=True)
    obrigatorio = ["DRT", "name", "Email", "numero_tel", "senha"]
    
    if not isinstance(dados, dict) or any(campo not in dados for campo in obrigatorio):
        return jsonify({"mensagem": "sem resultado, verifique os dados"}), 400
    
    DRT = dados["DRT"]
    name = dados["name"]
    Email = dados["Email"]
    numero_tel = dados["numero_tel"]
    senha = dados["senha"]
    
    drt_ok, mensagem = validar_DRT(DRT)
    if not drt_ok:
        return jsonify({"mensagem": mensagem}), 409
    
    if not validar_name(name):
        return jsonify({"mensagem": "verifique o nome"}), 400
    
    if not validar_email(Email):
        return jsonify({"mensagem": "email invalido"}), 400
    
    senha_ok, mensagem = validar_senha(senha)
    if not senha_ok:
        return jsonify({"mensagem": mensagem}), 400
    
    senha=criar_hash(senha)
    
    if not validar_telefone(numero_tel):
        return jsonify({"mensagem": "verifique o numero de telefone"}), 400
    
    with get_db() as conn:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO users(drt, name, email, numero_telefone, senha)
                VALUES (?, ?, ?, ?, ?)
            """, (DRT, name, Email, numero_tel, senha))
            conn.commit()
            return jsonify({"mensagem": "ok usuario cadastrado"}), 201
        except sqlite3.IntegrityError:
            return jsonify({"mensagem": "DRT ou email já cadastrados"}), 409
        except sqlite3.Error:
            return jsonify({"mensagem": "erro interno, tente mais tarde"}), 500