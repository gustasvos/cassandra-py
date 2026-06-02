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
    print('Insira os dados do produto:\n')
    nome = input("Nome: ")
    descricao = input("Descrição: ")
    try:
        preco = float(input("Preço: "))
    except ValueError:
        print("Preço inválido")
        return
    session.execute("INSERT INTO produto (id, nome, descricao, preco) VALUES (uuid(), %s, %s, %s)", (nome, descricao, preco))

def read_table_produto():
    create_table_produto()
    rows = list(session.execute("SELECT * FROM produto"))
    for i, row in enumerate(rows):
        print(f'{i} - {row}')
    print('=======================================')
    return rows

def update_produto():
    create_table_produto()
    rows = read_table_produto()
    if not rows:
        print('Nenhum produto encontrado')
        return
    
    i = int(input('Selecione o produto para atualizar: '))
    if i < 0 or i >= len(rows):
        print('Índice inválido')
        return

    produto_id = rows[i].id
    nome = input("Novo Nome: ")
    descricao = input("Nova Descrição: ")
    try:
        preco = float(input("Preço: "))
    except ValueError:
        print("Preço inválido")
        return
    session.execute("UPDATE produto SET nome = %s, descricao = %s, preco = %s WHERE id = %s", (nome, descricao, preco, produto_id))
    print(f"Produto {produto_id} atualizado com sucesso.")


def delete_produto():
    create_table_produto()
    rows = read_table_produto()
    if not rows:
        print('Nenhum produto encontrado')
        return
    
    i = int(input('Selecione o produto para deletar: '))
    if i < 0 or i >= len(rows):
        print('Índice inválido')
        return

    produto_id = rows[i].id
    session.execute("DELETE FROM produto WHERE id = %s", (produto_id,))
    print(f"Produto {produto_id} deletado com sucesso.")

    
# insert_produto()
# read_table_produto()
# delete_produto()
# read_table_produto()
# update_produto()