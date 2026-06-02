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
    print('Insira os dados do vendedor:\n')

    nome = input("Nome: ")
    cnpj = input("CNPJ: ")
    email = input("Email: ")
    senha = input("Senha: ")
    cep = input("CEP: ")
    cidade = input("Cidade: ")
    estado = input("Estado: ")
    rua = input("Rua: ")
    numero = input("Número: ")

    session.execute(
        """
        INSERT INTO vendedor (
            id, nome, cnpj, email, senha,
            cep, cidade, estado, rua, numero
        ) VALUES (
            uuid(), %s, %s, %s, %s,
            %s, %s, %s, %s, %s
        )
        """,
        (nome, cnpj, email, senha, cep, cidade, estado, rua, numero)
    )

def read_table_vendedor():
    create_table_vendedor()
    rows = list(session.execute("SELECT * FROM vendedor"))

    for i, row in enumerate(rows):
        print(f'{i} - {row}')

    print('=======================================')
    return rows

def update_vendedor():
    create_table_vendedor()

    rows = read_table_vendedor()
    if not rows:
        print('Nenhum vendedor encontrado')
        return

    i = int(input('Selecione o vendedor para atualizar: '))

    if i < 0 or i >= len(rows):
        print('Índice inválido')
        return

    vendedor_id = rows[i].id

    nome = input("Novo Nome: ")
    cnpj = input("Novo CNPJ: ")
    email = input("Novo Email: ")
    senha = input("Nova Senha: ")
    cep = input("Novo CEP: ")
    cidade = input("Nova Cidade: ")
    estado = input("Novo Estado: ")
    rua = input("Nova Rua: ")
    numero = input("Novo Número: ")

    session.execute(
        """
        UPDATE vendedor
        SET nome = %s,
            cnpj = %s,
            email = %s,
            senha = %s,
            cep = %s,
            cidade = %s,
            estado = %s,
            rua = %s,
            numero = %s
        WHERE id = %s
        """,
        (
            nome, cnpj, email, senha,
            cep, cidade, estado,
            rua, numero, vendedor_id
        )
    )

    print(f"Vendedor {vendedor_id} atualizado com sucesso.")

def delete_vendedor():
    create_table_vendedor()

    rows = read_table_vendedor()
    if not rows:
        print('Nenhum vendedor encontrado')
        return

    i = int(input('Selecione o vendedor para deletar: '))

    if i < 0 or i >= len(rows):
        print('Índice inválido')
        return

    vendedor_id = rows[i].id

    session.execute(
        "DELETE FROM vendedor WHERE id = %s",
        (vendedor_id,)
    )

    print(f"Vendedor {vendedor_id} deletado com sucesso.")