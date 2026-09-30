from flask import Flask,request,jsonify
import sqlite3
from app.DATABASE import get_db
from .Produtos_bp import produtos_bp

@produtos_bp.route("/estoque",methods=["GET"])
def  listar_estoque():
    
    try:
        with get_db() as conn:
            conn.row_factory= sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("""
                           SELECT
                           p.codigo_barras,
                           p.nome_produto,
                           p.valor_prod,
                           p.setor_id,
                           e.quantidade
                           FROM Produtos_cadastrados p 
                           JOIN estoque e ON p.codigo_barras = e.codigo_barras
                           """)
            produtos = cursor.fetchall()
            lista =[]
            for p in produtos:
                lista.append({
                   "codigo_barras":p["codigo_barras"],
                   "nome_produto": p["nome_produto"],
                   "valor_produto": p["valor_prod"],
                    "quantidade": p["quantidade"]
                })
            return jsonify(lista)
    except Exception as e:
        return  jsonify({"mensagem":f"erro: {e}"}),500

