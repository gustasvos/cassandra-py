from connect_database import connect_database
from produto import read_table_produto
from usuario import read_table_usuario
from vendedor import read_table_vendedor

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
                    frete FLOAT,
                    valor FLOAT)
    """)

def insert_compra():
    print('Selecione o usuário:\n')
    usuarios = read_table_usuario()
    if not usuarios:
        print('Nenhum usuário encontrado')
        return
    i_usuario = int(input('Índice do usuário: '))
    if i_usuario < 0 or i_usuario >= len(usuarios):
        print('Índice inválido')
        return

    print('Selecione o vendedor:\n')
    vendedores = read_table_vendedor()
    if not vendedores:
        print('Nenhum vendedor encontrado')
        return
    i_vendedor = int(input('Índice do vendedor: '))
    if i_vendedor < 0 or i_vendedor >= len(vendedores):
        print('Índice inválido')
        return

    print('Selecione o produto:\n')
    produtos = read_table_produto()
    if not produtos:
        print('Nenhum produto encontrado')
        return
    i_produto = int(input('Índice do produto: '))
    if i_produto < 0 or i_produto >= len(produtos):
        print('Índice inválido')
        return

    usuario = usuarios[i_usuario]
    vendedor = vendedores[i_vendedor]
    produto = produtos[i_produto]

    try:
        frete = float(input("Frete: "))
    except ValueError:
        print("Frete inválido")
        return

    valor = produto.preco + frete

    session.execute(
        """
        INSERT INTO compra (
            id, usuario_id, vendedor_id, produto_id,
            usuario_nome, vendedor_nome, produto_nome,
            produto_preco, frete, valor
        ) VALUES (uuid(), %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (
            usuario.id, vendedor.id, produto.id,
            usuario.nome, vendedor.nome, produto.nome,
            produto.preco, frete, valor
        )
    )
    print(f"Compra registrada: {usuario.nome} | {produto.nome} | {vendedor.nome} | {valor:.2f}")

def read_table_compra():
    rows = list(session.execute("SELECT * FROM compra"))
    for i, row in enumerate(rows):
        print(f'{i} - {row}')
    print('=======================================')
    return rows

def update_compra():
    rows = read_table_compra()
    if not rows:
        print('Nenhuma compra encontrada')
        return
    i = int(input('Selecione a compra para atualizar: '))
    if i < 0 or i >= len(rows):
        print('Índice inválido')
        return
    compra_id = rows[i].id

    print('Selecione o novo produto:\n')
    produtos = read_table_produto()
    if not produtos:
        print('Nenhum produto encontrado')
        return
    i_produto = int(input('Índice do novo produto: '))
    if i_produto < 0 or i_produto >= len(produtos):
        print('Índice inválido')
        return

    produto = produtos[i_produto]

    try:
        frete = float(input("Novo Frete: "))
    except ValueError:
        print("Frete inválido")
        return

    valor = produto.preco + frete

    session.execute(
        """
        UPDATE compra
        SET produto_id = %s,
            produto_nome = %s,
            produto_preco = %s,
            frete = %s,
            valor = %s
        WHERE id = %s
        """,
        (
            produto.id, produto.nome,
            produto.preco, frete, valor,
            compra_id
        )
    )
    print(f"Compra {compra_id} atualizada com sucesso.")

def delete_compra():
    rows = read_table_compra()
    if not rows:
        print('Nenhuma compra encontrada')
        return
    i = int(input('Selecione a compra para deletar: '))
    if i < 0 or i >= len(rows):
        print('Índice inválido')
        return
    compra_id = rows[i].id
    session.execute(
        "DELETE FROM compra WHERE id = %s",
        (compra_id,)
    )
    print(f"Compra {compra_id} deletada com sucesso.")