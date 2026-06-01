from connect_database import connect_database

session = connect_database()
session.set_keyspace("mercado_livre")

def create_table_usuario():
    session.execute("""
       CREATE TABLE IF NOT EXISTS usuario (
                    id UUID PRIMARY KEY,
                    nome TEXT,
                    email TEXT,
                    senha TEXT,
                    cpf TEXT,
                    cep TEXT,
                    cidade TEXT,
                    estado TEXT,
                    rua TEXT,
                    numero TEXT,
                    cartao TEXT
                    )
    """)

def insert_usuario():
    create_table_usuario()
    session.execute("""
        INSERT INTO cassandra_ex4.usuario (id, nome, email, senha, cpf, cep, cidade, estado, rua, numero, cartao) VALUES (uuid(), 'fone', 'um fone de ouvido', 45)
    """)

def read_table_usuario():
    create_table_usuario()
    # insert_usuario()
    rows = session.execute("SELECT * FROM cassandra_ex4.usuario")
    for row in rows:
        print(row)
    print('=======================================')

def update_usuario():
    create_table_usuario()


def delete_usuario():
    create_table_usuario()
    session.execute("DELETE FROM cassandra_ex4.usuario WHERE id = f0b82950-86a1-4890-81fe-56cbad53a5e8")


    
# insert_usuario()
read_table_usuario()
delete_usuario()
read_table_usuario()