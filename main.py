from favorito import insert_favorito, delete_favorito, read_table_favorito, update_favorito, create_table_favorito
from produto import insert_produto, delete_produto, update_produto, read_table_produto, create_table_produto
from usuario import insert_usuario, delete_usuario, update_usuario, read_table_usuario, create_table_usuario
from vendedor import insert_vendedor, delete_vendedor, update_vendedor, read_table_vendedor, create_table_vendedor
from compra import insert_compra, delete_compra, update_compra, read_table_compra, create_table_compra

acoes_crud = {
    "Usuario":   (insert_usuario,  read_table_usuario,  update_usuario,  delete_usuario),
    "Produto":   (insert_produto,  read_table_produto,  update_produto,  delete_produto),
    "Vendedor":  (insert_vendedor, read_table_vendedor, update_vendedor, delete_vendedor),
    "Compras":   (insert_compra,   read_table_compra,   update_compra,   delete_compra),
    "Favoritos": (insert_favorito, read_table_favorito, update_favorito, delete_favorito),
}

def menu_crud(col):
    insert, read, update, delete = acoes_crud[col]

    while True:
        print(f"\n{col.upper()}")
        print(f"1. Criar {col}")
        print(f"2. Ler {col}")

        if (update):
            print(f"3. Atualizar {col}")
            print(f"4. Deletar {col}")
            print(f"0. Voltar")
        else:
            print(f"3. Deletar {col}")
            print(f"0. Voltar")

        option = int(input("Escolha uma opção: "))
        print('\n')

        if (option == 1):
            insert()
        elif (option == 2):
            read()
        elif (option == 3):
            if update:
                update()
            else:
                delete()
        elif (option == 4 and update):
            delete()
        elif (option == 0):
            break
        else:
            print("Opção inválida")


def menu_cassandra():
    while True:
        print("MENU\n")
        print("ESCOLHA A TABELA PARA REALIZAR AS AÇÕES CRUD:\n")
        print("1. Usuario")
        print("2. Produtos")
        print("3. Vendedor")
        print("4. Compras")
        print("5. Favoritos")
        print("0. Sair")
        option = int(input("Escolha uma opção: "))

        if (option == 1):
            create_table_usuario()
            menu_crud("Usuario")
        elif (option == 2):
            create_table_produto()
            menu_crud("Produto")
        elif (option == 3):
            create_table_vendedor()
            menu_crud("Vendedor")
        elif (option == 4):
            create_table_compra()
            menu_crud("Compras")
        elif (option == 5):
            create_table_favorito()
            menu_crud("Favoritos")
        elif (option == 0):
            print("Saindo.")
            break
        else:
            print("Opção inválida")
        
menu_cassandra()