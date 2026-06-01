from connect_database import connect_database

session = connect_database()
session.set_keyspace("mercado_livre")

def create_table_vendedor():
    session.execute("""
       CREATE TABLE IF NOT EXISTS vendedor (
                    id UUID PRIMARY KEY,
                    nome TEXT,
                    cnpj TEXT,
                    email TEXT,
                    senha TEXT,
                    cep TEXT,
                    cidade TEXT,
                    estado TEXT,
                    rua TEXT,
                    numero TEXT
                    )
    """)

def insert_vendedor():
    create_table_vendedor()
    session.execute("""
        INSERT INTO cassandra_ex4.vendedor (id, nome, cnpj, email, senha, cep, cidade, estado, rua, numero) VALUES (uuid(), 'fone', 'um fone de ouvido', 45)
    """)

def read_table_vendedor():
    create_table_vendedor()
    # insert_vendedor()
    rows = session.execute("SELECT * FROM cassandra_ex4.vendedor")
    for row in rows:
        print(row)
    print('=======================================')

def update_vendedor():
    create_table_vendedor()


def delete_vendedor():
    create_table_vendedor()
    session.execute("DELETE FROM cassandra_ex4.vendedor WHERE id = f0b82950-86a1-4890-81fe-56cbad53a5e8")


    
# insert_vendedor()
read_table_vendedor()
delete_vendedor()
read_table_vendedor()