from flask import blueprints ,request, jsonify
from app.models.produto import Produto
from app.services.service_pra_produto.buscar import buscar
from .Produtos_bp import produtos_bp



@produtos_bp.route("/EditarValor", methods=["POST"])
def ajustar_valor_produto():
    requisicao = request.get_json()

    if not requisicao.get("codigo_barras") or not requisicao.get("novo_valor"):
        return jsonify({"mensagem": "verifique os campos e tente novamente"}), 400

    try:
        produto_existe = buscar(requisicao["codigo_barras"])
        if not produto_existe:
            return jsonify({"mensagem": "produto não encontrado"}), 404

        valor = float(requisicao["novo_valor"])
        if valor < 0:
            return jsonify({"mensagem": "Erro verifique se o novo valor é válido"}), 400

        codigo_barras = requisicao["codigo_barras"]

    except (TypeError, ValueError):
        return jsonify({"mensagem": "verifique os campos e tente novamente"}), 400

    #  função que atualiza o banco
    ajuste_devalor = Produto.editar_valor_produto(codigo_barras, valor)

    if not ajuste_devalor:
        return jsonify({"mensagem": "erro verifique os campos e tente novamente"}), 400
    else:
        return jsonify({"mensagem": "ok valor inserido com sucesso"}), 200
