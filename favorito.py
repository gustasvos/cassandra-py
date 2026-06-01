from connect_database import connect_database

session = connect_database()
session.set_keyspace("mercado_livre")

def create_table_favorito():
    session.execute("""
       CREATE TABLE IF NOT EXISTS favorito (
                    id UUID,
                    usuario_id UUID,
                    produto_id UUID,
                    usuario_nome TEXT,
                    produto_nome TEXT,
                    produto_descricao TEXT,
                    produto_preco FLOAT,
                    PRIMARY KEY (usuario_id, produto_id)
                    )
    """)

def insert_favorito():
    create_table_favorito()
    session.execute("""
        INSERT INTO cassandra_ex4.favorito (id, usuario_id, produto_id, usuario_nome, produto_nome, produto_descricao, produto_preco) VALUES (uuid(), 'fone', 'um fone de ouvido', 45)
    """)

def read_table_favorito():
    create_table_favorito()
    # insert_favorito()
    rows = session.execute("SELECT * FROM cassandra_ex4.favorito")
    for row in rows:
        print(row)
    print('=======================================')

def update_favorito():
    create_table_favorito()


def delete_favorito():
    create_table_favorito()
    session.execute("DELETE FROM cassandra_ex4.favorito WHERE id = f0b82950-86a1-4890-81fe-56cbad53a5e8")


    
# insert_favorito()
read_table_favorito()
delete_favorito()
read_table_favorito()