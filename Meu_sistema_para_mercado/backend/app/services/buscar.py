
from app.DATABASE import get_db


def buscar(codigo_barras):
    try:
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT p.codigo_barras
                FROM Produtos_cadastrados p
                WHERE p.codigo_barras = ?
            """, (codigo_barras,))
            resultado = cursor.fetchone()

            if resultado:
                return True   # produto encontrado
            else:
                return False  # produto não encontrado

    except Exception as e:
        print("Erro", e)
        return None #erro inesperado