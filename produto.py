from connect_database import connect_database

session = connect_database()
session.set_keyspace("mercado_livre")

def create_table_produto():
    session.execute("""
       CREATE TABLE IF NOT EXISTS produto (
                    id UUID PRIMARY KEY,
                    nome TEXT,
                    descricao TEXT,
                    preco FLOAT)
    """)

def insert_produto():
    session.execute("""
        INSERT INTO cassandra_ex4.produto (id, nome, descricao, preco) VALUES (uuid(), 'fone', 'um fone de ouvido', 45)
    """)

def read_table_produto():
    create_table_produto()
    insert_produto()
    rows = session.execute("SELECT * FROM produto")
    for row in rows:
        print(row)

read_table_produto()