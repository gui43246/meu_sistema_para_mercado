import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "banco.db")

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS setor(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            nome_setor TEXT NOT NULL)""")

        cursor.execute("""CREATE TABLE IF NOT EXISTS Produtos_cadastrados(
            codigo_barras TEXT PRIMARY KEY NOT NULL,
            nome_produto TEXT NOT NULL,
            valor_prod REAL NOT NULL,
            setor_id INTEGER NOT NULL,
            FOREIGN KEY (setor_id) REFERENCES setor(id))""")

        cursor.execute("""CREATE TABLE IF NOT EXISTS estoque(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            codigo_barras TEXT UNIQUE NOT NULL,
            quantidade INTEGER NOT NULL DEFAULT 0,
            FOREIGN KEY (codigo_barras) REFERENCES Produtos_cadastrados(codigo_barras))""")

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

if __name__ == "__main__":
    init_db()
    print("Banco de dados inicializado com sucesso!")



