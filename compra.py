from connect_database import connect_database

session = connect_database()
session.set_keyspace("mercado_livre")

def create_table_compra():
    session.execute("""
       CREATE TABLE IF NOT EXISTS compra (
                    id UUID PRIMARY KEY,
                    usuario_id UUID,
                    vendedor_id UUID,
                    produto_id UUID,
                    usuario_nome TEXT,
                    vendedor_nome TEXT,
                    produto_nome TEXT,
                    produto_preco FLOAT,
                    frete  FLOAT,
                    valor FLOAT
                    )
    """)

def insert_compra():
    create_table_compra()
    session.execute("""
        INSERT INTO cassandra_ex4.compra (id, usuario_id, vendedor_id, produto_id, usuario_nome, vendedor_nome, produto_nome, produto_preco, frete, valor) VALUES (uuid(), 'fone', 'um fone de ouvido', 45)
    """)

def read_table_compra():
    create_table_compra()
    # insert_compra()
    rows = session.execute("SELECT * FROM cassandra_ex4.compra")
    for row in rows:
        print(row)
    print('=======================================')

def update_compra():
    create_table_compra()


def delete_compra():
    create_table_compra()
    session.execute("DELETE FROM cassandra_ex4.compra WHERE id = 032225fd-58ee-494e-8154-05be74543536")


    
# insert_compra()
read_table_compra()
delete_compra()
read_table_compra()