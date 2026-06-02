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
    print('Insira os dados do usuário:\n')

    nome = input("Nome: ")
    email = input("Email: ")
    senha = input("Senha: ")
    cpf = input("CPF: ")
    cep = input("CEP: ")
    cidade = input("Cidade: ")
    estado = input("Estado: ")
    rua = input("Rua: ")
    numero = input("Número: ")
    cartao = input("Cartão: ")

    session.execute(
        """
        INSERT INTO usuario (
            id, nome, email, senha, cpf,
            cep, cidade, estado, rua, numero, cartao
        ) VALUES (
            uuid(), %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s
        )
        """,
        (
            nome, email, senha, cpf,
            cep, cidade, estado,
            rua, numero, cartao
        )
    )

def read_table_usuario():
    create_table_usuario()

    rows = list(session.execute("SELECT * FROM usuario"))

    for i, row in enumerate(rows):
        print(f'{i} - {row}')

    print('=======================================')
    return rows

def update_usuario():
    create_table_usuario()

    rows = read_table_usuario()
    if not rows:
        print('Nenhum usuário encontrado')
        return

    i = int(input('Selecione o usuário para atualizar: '))

    if i < 0 or i >= len(rows):
        print('Índice inválido')
        return

    usuario_id = rows[i].id

    nome = input("Novo Nome: ")
    email = input("Novo Email: ")
    senha = input("Nova Senha: ")
    cpf = input("Novo CPF: ")
    cep = input("Novo CEP: ")
    cidade = input("Nova Cidade: ")
    estado = input("Novo Estado: ")
    rua = input("Nova Rua: ")
    numero = input("Novo Número: ")
    cartao = input("Novo Cartão: ")

    session.execute(
        """
        UPDATE usuario
        SET nome = %s,
            email = %s,
            senha = %s,
            cpf = %s,
            cep = %s,
            cidade = %s,
            estado = %s,
            rua = %s,
            numero = %s,
            cartao = %s
        WHERE id = %s
        """,
        (
            nome, email, senha, cpf,
            cep, cidade, estado,
            rua, numero, cartao,
            usuario_id
        )
    )

    print(f"Usuário {usuario_id} atualizado com sucesso.")

def delete_usuario():
    create_table_usuario()

    rows = read_table_usuario()
    if not rows:
        print('Nenhum usuário encontrado')
        return

    i = int(input('Selecione o usuário para deletar: '))

    if i < 0 or i >= len(rows):
        print('Índice inválido')
        return

    usuario_id = rows[i].id

    session.execute(
        "DELETE FROM usuario WHERE id = %s",
        (usuario_id,)
    )

    print(f"Usuário {usuario_id} deletado com sucesso.")