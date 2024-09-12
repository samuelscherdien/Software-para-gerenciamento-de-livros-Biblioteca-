# Mensagem de Boas-Vindas
print('Bem-vindo à Biblioteca do Samuel!')

# Listas e variáveis globais
livros = []
clientes = []
id_livro_global = 0
id_cliente_global = 0

# Função para cadastrar livro
def cadastrar_livro():
    global id_livro_global
    id_livro_global += 1
    print('-' * 48)
    print('MENU CADASTRAR LIVRO')
    nome = input('Digite o nome do livro: ')
    autor = input('Digite o autor do livro: ')
    editora = input('Digite a editora do livro: ')

    livro = {'ID': id_livro_global, 'Nome': nome, 'Autor': autor, 'Editora': editora, 'Emprestado': False}
    livros.append(livro)

    print('Livro cadastrado com sucesso.')

# Função para consultar livros
def consultar_livro():
    print('-' * 48)
    print('MENU CONSULTAR LIVRO')
    opcao = int(input('Escolha uma opção: \n'
                      '1. Consultar todos os Livros\n'
                      '2. Consultar por ID\n'
                      '3. Consultar por Autor\n'
                      '4. Retornar ao menu\n'
                      '>> '))
    if opcao == 1:
        if livros:
            for livro in livros:
                status = 'Emprestado' if livro['Emprestado'] else 'Disponível'
                print('-' * 24)
                print(f'ID: {livro["ID"]} \n'
                      f'Nome: {livro["Nome"]} \n'
                      f'Autor: {livro["Autor"]} \n'
                      f'Editora: {livro["Editora"]} \n'
                      f'Status: {status}')
                print('-' * 24)
        else:
            print('Nenhum livro cadastrado.')

    elif opcao == 2:
        id_consulta = int(input('Digite o ID do livro: '))
        encontrado = False
        for livro in livros:
            if livro["ID"] == id_consulta:
                status = 'Emprestado' if livro['Emprestado'] else 'Disponível'
                print('-' * 24)
                print(f'ID: {livro["ID"]} \n'
                      f'Nome: {livro["Nome"]} \n'
                      f'Autor: {livro["Autor"]} \n'
                      f'Editora: {livro["Editora"]} \n'
                      f'Status: {status}')
                print('-' * 24)
                encontrado = True
                break
        if not encontrado:
            print('Livro não encontrado.')

    elif opcao == 3:
        autor_consulta = input('Digite o Autor do livro: ')
        encontrado = False
        for livro in livros:
            if livro['Autor'].lower() == autor_consulta.lower():
                status = 'Emprestado' if livro['Emprestado'] else 'Disponível'
                print('-' * 24)
                print(f'ID: {livro["ID"]} \n'
                      f'Nome: {livro["Nome"]} \n'
                      f'Autor: {livro["Autor"]} \n'
                      f'Editora: {livro["Editora"]} \n'
                      f'Status: {status}')
                print('-' * 24)
                encontrado = True
        if not encontrado:
            print(f'Nenhum livro encontrado para o autor "{autor_consulta}".')

    elif opcao == 4:
        return
    else:
        print('Opção inválida. Tente novamente.')

# Função para remover livro
def remover_livro():
    print('-' * 48)
    print('MENU REMOVER LIVRO')
    id_remover = int(input("Digite o ID do livro a ser removido: "))
    for livro in livros:
        if livro['ID'] == id_remover:
            livros.remove(livro)
            print("Livro removido com sucesso.")
            return
    print("ID inválido.")

# Função para cadastrar cliente
def cadastrar_cliente():
    global id_cliente_global
    id_cliente_global += 1
    print('-' * 48)
    print('MENU CADASTRAR CLIENTE')
    nome = input('Digite o nome do cliente: ')
    email = input('Digite o email do cliente: ')

    cliente = {'ID': id_cliente_global, 'Nome': nome, 'Email': email}
    clientes.append(cliente)

    print('Cliente cadastrado com sucesso.')

# Função para consultar clientes
def consultar_cliente():
    print('-' * 48)
    print('MENU CONSULTAR CLIENTE')
    opcao = int(input('Escolha uma opção: \n'
                      '1. Consultar todos os Clientes\n'
                      '2. Consultar por ID\n'
                      '3. Retornar ao menu\n'
                      '>> '))
    if opcao == 1:
        if clientes:
            for cliente in clientes:
                print('-' * 24)
                print(f'ID: {cliente["ID"]} \n'
                      f'Nome: {cliente["Nome"]} \n'
                      f'Email: {cliente["Email"]}')
                print('-' * 24)
        else:
            print('Nenhum cliente cadastrado.')

    elif opcao == 2:
        id_consulta = int(input('Digite o ID do cliente: '))
        encontrado = False
        for cliente in clientes:
            if cliente["ID"] == id_consulta:
                print('-' * 24)
                print(f'ID: {cliente["ID"]} \n'
                      f'Nome: {cliente["Nome"]} \n'
                      f'Email: {cliente["Email"]}')
                print('-' * 24)
                encontrado = True
                break
        if not encontrado:
            print('Cliente não encontrado.')

    elif opcao == 3:
        return
    else:
        print('Opção inválida. Tente novamente.')

# Função para emprestar livro
def emprestar_livro():
    id_livro = int(input('Digite o ID do livro a ser emprestado: '))
    id_cliente = int(input('Digite o ID do cliente que está emprestando o livro: '))

    livro_encontrado = False
    cliente_encontrado = False

    for livro in livros:
        if livro["ID"] == id_livro:
            livro_encontrado = True
            if livro['Emprestado']:
                print('O livro já está emprestado.')
            else:
                livro['Emprestado'] = True
                print(f'Livro ID {id_livro} emprestado com sucesso.')
            break

    if not livro_encontrado:
        print('Livro não encontrado.')

    for cliente in clientes:
        if cliente["ID"] == id_cliente:
            cliente_encontrado = True
            break

    if not cliente_encontrado:
        print('Cliente não encontrado.')

# Função para devolver livro
def devolver_livro():
    id_livro = int(input('Digite o ID do livro a ser devolvido: '))

    livro_encontrado = False

    for livro in livros:
        if livro["ID"] == id_livro:
            livro_encontrado = True
            if not livro['Emprestado']:
                print('O livro não está emprestado.')
            else:
                livro['Emprestado'] = False
                print(f'Livro ID {id_livro} devolvido com sucesso.')
            break

    if not livro_encontrado:
        print('Livro não encontrado.')

# Função principal
def main():
    while True:
        print('-' * 48)
        print('MENU PRINCIPAL')
        opcao = input('Escolha uma opção: \n'
                      '1. Cadastrar Livro\n'
                      '2. Consultar Livro(s)\n'
                      '3. Remover Livro\n'
                      '4. Cadastrar Cliente\n'
                      '5. Consultar Cliente(s)\n'
                      '6. Emprestar Livro\n'
                      '7. Devolver Livro\n'
                      '8. Sair\n'
                      '>> ')
        try:
            opcao = int(opcao)
            if opcao == 1:
                cadastrar_livro()
            elif opcao == 2:
                consultar_livro()
            elif opcao == 3:
                remover_livro()
            elif opcao == 4:
                cadastrar_cliente()
            elif opcao == 5:
                consultar_cliente()
            elif opcao == 6:
                emprestar_livro()
            elif opcao == 7:
                devolver_livro()
            elif opcao == 8:
                print('Encerrando o programa.')
                break
            else:
                print('Opção inválida.')
        except ValueError:
            print('Por favor, digite um número válido.')

# Chamada da função main para iniciar o programa
if __name__ == '__main__':
    main()
