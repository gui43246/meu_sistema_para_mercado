from flask import  request, jsonify
from app.DATABASE import get_db
import sqlite3
from app.models.produto import Produto
from .Produtos_bp import produtos_bp
from app.services.buscar import buscar

@produtos_bp.route('/cadastrar', methods=["POST"])
def cadastrar_produto():
    conn = None
    try:
        conn = get_db()
        cursor = conn.cursor()
        dados = request.get_json()
        campos_obrigatorios = ["codigo_barras","nome_produto","valor_prod","setor_id"]
        faltando = [campo for campo in campos_obrigatorios if not campo in dados]
        if faltando:
            return jsonify({"mensagem": f"faltando o campo {','.join(faltando)}"}),400
        
        try:
            dados["valor_prod"] = float(dados["valor_prod"])
            dados["setor_id"] = int(dados["setor_id"])
        except ValueError:
            return jsonify({"mensagem": "Campo inválido: valor_prod ou setor_id"}), 422
        
        produto_existe=buscar(dados["codigo_barras"])
        
        if not produto_existe:
            
            NOVO_PRODUTO = Produto(codigo_barras=dados["codigo_barras"],nome_produto=dados["nome_produto"],valor_produto=dados["valor_prod"],setor=dados["setor_id"])
            
            cursor.execute("""
                INSERT INTO Produtos_cadastrados(
                    codigo_barras,
                    nome_produto,
                    valor_prod,
                    setor_id
                ) VALUES (?, ?, ?, ?)
            """, (
                NOVO_PRODUTO.codigo_barras,
                NOVO_PRODUTO.nome_produto,
                NOVO_PRODUTO.valor_produto,
                NOVO_PRODUTO.setor
            ))
            cursor.execute("""INSERT INTO estoque(
                codigo_barras
                )VALUES(?)""", 
                (NOVO_PRODUTO.codigo_barras,))
                                    
            conn.commit()
            return jsonify({"mensagem": "Sucesso ao cadastrar item"}), 201
        else:
            return jsonify({"mensagem":"produto ja cadastrado com esse codigo de barras"}),501
            
    except sqlite3.Error as e:
        return jsonify({"mensagem": f"Erro inespeado tenta novamente mais tarde: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"mensagem": f"Erro inesperado, verifique os campos e tente novamnete "}), 500
    finally:
        if conn:
            conn.close()

        