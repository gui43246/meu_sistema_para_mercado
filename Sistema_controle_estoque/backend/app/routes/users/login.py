from flask import request,jsonify
from app.DATABASE import get_db
import sqlite3
from app.routes.users.Users_bp import users_bp
from app.security.verificar_hash import verifique_hash

@users_bp.route("/login",methods=["POST"])
def login():
    dados = request.get_json(silent=True)
    dados_esperados = ["drt", "senha_digitada"]

    if not isinstance(dados, dict) or any(dado not in dados for dado in dados_esperados):
        return jsonify({"mensagem": "Verifique os dados e tente novamente"}), 400

    drt = dados["drt"]
    senha_digitada = dados["senha_digitada"]

    with get_db() as conn:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT drt, senha 
                FROM users
                WHERE drt = ?
            """, (drt,))
            resultado = cursor.fetchone()

            if not resultado:
                return jsonify({"mensagem": "Usuario sem registro"}), 404

            senha_armazenada= resultado[1]
            if  verifique_hash(senha_digitada,senha_armazenada):
                return jsonify({"sucesso":True}),200
            else:
                return jsonify({"erro": "Senha incorreta"}), 401

        except (sqlite3.Error, Exception):
            return jsonify({"erro": "Erro interno, tente novamente mais tarde"}), 500