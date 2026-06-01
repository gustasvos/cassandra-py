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
    create_table_produto()
    session.execute("""
        INSERT INTO cassandra_ex4.produto (id, nome, descricao, preco) VALUES (uuid(), 'fone', 'um fone de ouvido', 45)
    """)

def read_table_produto():
    create_table_produto()
    # insert_produto()
    rows = session.execute("SELECT * FROM cassandra_ex4.produto")
    for i, row in enumerate(rows):
        print(f'{i} - {row}')
    print('=======================================')

def update_produto():
    create_table_produto()


def delete_produto():
    create_table_produto()
    session.execute("DELETE FROM cassandra_ex4.produto WHERE id = 032225fd-58ee-494e-8154-05be74543536")


    
# insert_produto()
read_table_produto()
delete_produto()
read_table_produto()