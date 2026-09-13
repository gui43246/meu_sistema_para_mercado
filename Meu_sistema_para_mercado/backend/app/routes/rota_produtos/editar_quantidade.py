from flask import request, jsonify
from app.models.produto import Produto
from app.services.service_pra_produto.buscar import buscar
from .Produtos_bp import produtos_bp


@produtos_bp.route("/EditarQuantidade", methods=["POST"])
def editar_produtos():
    dados = request.get_json(silent=True)  # recebe codigo de barras e quantidade

    if not isinstance(dados, dict) or "codigo_barras" not in dados or "quantidade" not in dados:
        return jsonify({"mensagem": "não autorizado, campo incorreto"}), 400

    codigo_barras = dados["codigo_barras"]

    try:
        quantidade = int(dados["quantidade"])
    except (ValueError, TypeError):
        return jsonify({"mensagem": "quantidade inválida"}), 422

    produto_existe = buscar(codigo_barras)
    if not produto_existe:
        return jsonify({"mensagem": "sem resultado, produto não existe"}), 404

    sucesso = Produto.ajustar_quantidade(codigo_barras, quantidade)

    if not sucesso:
        return jsonify({"mensagem": "erro inesperado, tente novamente"}), 500

    return jsonify({"mensagem": "ok, quantidade ajustada"}), 200