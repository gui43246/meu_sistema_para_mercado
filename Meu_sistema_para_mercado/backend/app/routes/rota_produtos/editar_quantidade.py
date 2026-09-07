from flask import blueprints ,request, jsonify
from models.produto import Produto
from .Produtos_bp import produtos_bp

@produtos_bp.route("/EditarQuantidade",methods=["POST"])
def editar_produtos():
    requisição = request.get_json() #receber codigo de barras e quantidade 
    if not requisição:
            return jsonify ({"mensagem": f"campo vazio"}),404
    codigo_barras = requisição["codigo_barras"]
    quantidade = requisição['quantidade']
    
    produto =Produto.buscar(requisição["codigo_barras"])
    if produto is  None:
        return jsonify ({"mensagem":f"Produto não encontrado"}),404
    try:
        resultado=produto.ajustar_quantidade(quantidade)
        if resultado is None:
            return jsonify ({"mensagem":f"erro na quantidade de itens"}),404
        return jsonify({"mensagem":f"sucesso, nova quantidade adicionada"}),200
    except Exception as e:
        return jsonify ({"mensagem":f"erro {e}"}),404