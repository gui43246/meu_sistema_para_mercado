from app.DATABASE import get_db
from typing import Optional

class Produto:
    def __init__(self, codigo_barras, nome_produto, valor_produto, setor,quantidade=0):
        self.codigo_barras = codigo_barras
        self.nome_produto = nome_produto
        self.valor_produto = valor_produto
        self.setor = setor
        self.quantidade = quantidade

    def ajustar_quantidade(self, quantidade):
        if quantidade < 0:
            return None
        try:
            with get_db() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    UPDATE estoque
                    SET quantidade = ?
                    WHERE codigo_barras = ?
                """, (quantidade, self.codigo_barras))
                conn.commit()
            self.quantidade = quantidade
            return True
        except Exception:
            return None

    def ajustar_valor_produto(self, novo_valor):
        if novo_valor < 0:
            return False
        try:
            with get_db() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    UPDATE Produtos_cadastrados
                    SET valor_prod = ?
                    WHERE codigo_barras = ?
                """, (novo_valor, self.codigo_barras))
                conn.commit()
            self.valor_produto = novo_valor
            return True
        except Exception:
            return False

    def ajustar_setor_produto(self, novo_setor):
        try:
            with get_db() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    UPDATE Produtos_cadastrados
                    SET setor_id = ?
                    WHERE codigo_barras = ?
                """, (novo_setor, self.codigo_barras))
                conn.commit()
            self.setor = novo_setor
            return True
        except Exception:
            return False
    @classmethod
    def buscar(cls, codigo_barras: str ) -> Optional["Produto"]:
        try:
            with get_db() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT codigo_barras, nome_produto, valor_prod, setor_id, quantidade
                    FROM Produtos_cadastrados
                    WHERE codigo_barras = ?
                """, (codigo_barras,))
                resultado = cursor.fetchone()
                if not resultado:
                    return None
                return cls(
                    codigo_barras=resultado[0],
                    nome_produto=resultado[1],
                    valor_produto=resultado[2],
                    setor=resultado[3],
                    quantidade=resultado[4]
                )
        except Exception as e:
            return None