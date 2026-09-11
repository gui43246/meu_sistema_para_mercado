from flask import request, jsonify
from .Produtos_bp import produtos_bp
from app.services.buscar import buscar
from app.models.produto import Produto


@produtos_bp.route("/ajuste_setor_produto", methods=["POST"])
def ajuste_setor():
    dados = request.get_json(silent=True)

    if not isinstance(dados, dict) or not dados.get("codigo_barras") or not dados.get("novo_setor"):
        return jsonify({"mensagem": "erro: verifique os campos e tente novamente"}), 400

    codigo_barras = dados["codigo_barras"]
    setor = dados["novo_setor"]

    produto_existe = buscar(codigo_barras)
    if not produto_existe:
        return jsonify({"mensagem": "erro: produto não encontrado"}), 404

    sucesso, codigo = Produto.setor_ajustar(codigo_barras, setor)

    if not sucesso:
        return jsonify({"mensagem": "erro: verifique e tente novamente"}), 500

    return jsonify({"mensagem": "sucesso: setor ajustado"}), 200