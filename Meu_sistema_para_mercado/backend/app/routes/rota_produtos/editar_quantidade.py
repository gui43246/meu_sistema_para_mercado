from flask import blueprints ,request, jsonify
from app.DATABASE import get_db
import sqlite3
from app import app
from Meu_sistema_para_mercado.backend.models.produto import Produto
from app.routes.rota_produtos import Produtos_bp

@Produtos_bp.route("/EditarQuantidade",methods=["POST"])
def editar_produtos():
    requisição = request.get_json() #receber codigo de barras e quantidade 
    if not requisição:
            return jsonify ({"mensagem": f"campo vazio"}),404
    codigo_barras = requisição["codigo_barras"]
    quantidade = requisição['quantidade']
    
    Produto = Produto.buscar(requisição["codigo_barras"])
    if Produto is  None:
        return jsonify ({"mensagem":f"Produto não encontrado"}),404
    try:
        Produto.ajustar_quantidade(codigo_barras,quantidade)
        if Produto is None:
            return jsonify ({"mensagem":f"erro na quantidade de itens"}),404
        return jsonify({"mensagem":f"sucesso, nova quantidade adicionada"}),200
    except Exception as e:
        return jsonify ({"mensagem":f"erro {e}"}),404