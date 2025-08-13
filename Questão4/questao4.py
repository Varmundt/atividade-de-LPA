print("Bem-vindo a Empresa de Mauricio Miller")

# Variavel de ID e Lista vazia
id_global = 5420907
lista_funcionarios = []
def cadastrar_funcionario(id):
    print("\n--- MENU CADASTRAR FUNCIONÁRIO ---")
    print("---------------------------------------------")
    print("Id do Funcionário: {}".format(id))
    nome = input("Por favor entre com o nome do Funcionário: ")
    setor = input("Por favor entre com o setor do Funcionário: ")
    salario = float(input("Por favor entre com o salário do Funcionário: "))
    funcionario = {"id": id,"nome": nome,"setor": setor,"salario": salario}
    lista_funcionarios.append(funcionario.copy())
# Função de consulta de funcionario
def consultar_funcionarios():
    while True:
        print("\n--- MENU CONSULTAR FUNCIONÁRIOS ---")
        print("---------------------------------------------")
        print("Escolha a opção desejada:")
        print("1 - Consultar todos os Funcionários")
        print("2 - Consultar Funcionário por id")
        print("3 - Consultar Funcionário por setor")
        print("4 - Retornar")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            print("\nLista de todos os funcionários:")
            for func in lista_funcionarios:
                print(func)
        elif opcao == "2":
            try:
                id_busca = int(input("Digite o ID do funcionário: "))
                encontrado = False
                for func in lista_funcionarios:
                    if func["id"] == id_busca:
                        print(func)
                        encontrado = True
                if not encontrado:
                    print("ID não encontrado.")
            except ValueError:
                print("Digite um número válido.")
        elif opcao == "3":
            setor_busca = input("Digite o setor: ")
            encontrado = False
            for func in lista_funcionarios:
                if func["setor"].lower() == setor_busca.lower():
                    print(func)
                    encontrado = True
            if not encontrado:
                print("Nenhum funcionário encontrado nesse setor.")
        elif opcao == "4":
            return  # Volta pro menu
        else:
            print("Opção inválida.")
# Função para Remover um funcionario
def remover_funcionario():
    while True:
        try:
            print("\n--- MENU REMOVER FUNCIONÁRIOS ---")
            print("---------------------------------------------")
            id_remove = int(input("Digite o ID do funcionário a ser removido: "))
            for func in lista_funcionarios:
                if func["id"] == id_remove:
                    lista_funcionarios.remove(func)
                    print("Funcionário removido com sucesso!")
                    return
                print("ID inválido.")
        except ValueError:
            print("Digite um número válido.")
# Menu
while True:
    print("-- Menu Principal ---")
    print("---------------------------------------------")
    print("Escolha a opção desejada:")
    print("1 - Cadastrar Funcionários")
    print("2 - Consultar Funcionário(s)")
    print("3 - Remover Funcionário")
    print("4 - Sair")
    opcao = input(">>>")
    if opcao == "1":
        cadastrar_funcionario(id_global)
        id_global += 1
    elif opcao == "2":
        consultar_funcionarios()
    elif opcao == "3":
        remover_funcionario()
    elif opcao == "4":
        print("Saindo!")
        break
    else:print("Opção inválida, tente novamente!")