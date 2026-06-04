from connect_database import connect_database
from produto import read_table_produto
from usuario import read_table_usuario

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
                    PRIMARY KEY (usuario_id, produto_id))
    """)

def insert_favorito():
    print('Selecione o usuário:\n')
    usuarios = read_table_usuario()
    if not usuarios:
        print('Nenhum usuário encontrado')
        return
    i_usuario = int(input('Índice do usuário: '))
    if i_usuario < 0 or i_usuario >= len(usuarios):
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
    produto = produtos[i_produto]

    session.execute(
        """
        INSERT INTO favorito (
            id, usuario_id, produto_id,
            usuario_nome, produto_nome,
            produto_descricao, produto_preco
        ) VALUES (uuid(), %s, %s, %s, %s, %s, %s)
        """,
        (
            usuario.id, produto.id,
            usuario.nome, produto.nome,
            produto.descricao, produto.preco
        )
    )
    print(f"Favorito adicionado: {usuario.nome} -> {produto.nome}")

def read_table_favorito():
    rows = list(session.execute("SELECT * FROM favorito"))
    for i, row in enumerate(rows):
        print(f'{i} - {row}')
    print('=======================================')
    return rows

def update_favorito():
    rows = read_table_favorito()
    if not rows:
        print('Nenhum favorito encontrado')
        return
    i = int(input('Selecione o favorito para atualizar: '))
    if i < 0 or i >= len(rows):
        print('Índice inválido')
        return

    usuario_id = rows[i].usuario_id
    produto_id = rows[i].produto_id

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

    session.execute(
        """
        UPDATE favorito
        SET produto_nome = %s,
            produto_descricao = %s,
            produto_preco = %s
        WHERE usuario_id = %s AND produto_id = %s
        """,
        (
            produto.nome, produto.descricao, produto.preco,
            usuario_id, produto_id
        )
    )
    print(f"Favorito ({usuario_id} / {produto_id}) atualizado com sucesso.")

def delete_favorito():
    rows = read_table_favorito()
    if not rows:
        print('Nenhum favorito encontrado')
        return
    i = int(input('Selecione o favorito para deletar: '))
    if i < 0 or i >= len(rows):
        print('Índice inválido')
        return
    usuario_id = rows[i].usuario_id
    produto_id = rows[i].produto_id
    session.execute(
        "DELETE FROM favorito WHERE usuario_id = %s AND produto_id = %s",
        (usuario_id, produto_id)
    )
    print(f"Favorito ({usuario_id} / {produto_id}) deletado com sucesso.")