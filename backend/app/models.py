from app.DATABASE import get_db

class Produto:
    def __init__(self, codigo_barras, nome_produto, valor_produto, setor):
        self.codigo_barras = codigo_barras
        self.nome_produto = nome_produto
        self.valor_produto = valor_produto
        self.setor = setor
        self.quantidade = 0

    def ajustar_quantidade(self, quantidade):
        if quantidade < 0:
            return False
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
            return False

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
