from backend.app.DATABASE import get_db

def testar_busca():
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT p.codigo_barras,
                   p.nome_produto,
                   p.valor_prod,
                   p.setor,
                   COALESCE(e.quantidade,0) as quantidade
            FROM Produtos_cadastrados p
            LEFT JOIN estoque e ON p.codigo_barras = e.codigo_barras
            WHERE p.codigo_barras = '7891234567890';
        """)
        resultado = cursor.fetchone()
        print(resultado)  # mostra o que veio do banco
    except Exception as e:
        print(f"Erro na consulta: {e}")
    finally:
        conn.close()
