def inserir(lista, linguagem):
    lista.append(linguagem)

def buscar(lista, linguagem):
    return linguagem in lista

def remover(lista, linguagem, linguagens_removidas):
    if linguagem in lista:
        lista.remove(linguagem)
        linguagens_removidas.append(linguagem)
        return True
    return False

def listar_linguagens(lista):
    return lista

def interface_usuario():
    linguagens = []
    linguagens_removidas = []

    while True:
        print("\nMenu:")
        print("1-> Inserir uma linguagem")
        print("2-> Remover uma linguagem")
        print("3-> Buscar uma linguagem")
        print("4-> Listar todas as linguagens cadastradas")
        print("5-> Listar linguagens removidas")
        print("6-> Sair do programa")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            linguagem = input("Digite o nome da linguagem a inserir: ")
            inserir(linguagens, linguagem)
            print("{} inserida com sucesso.".format(linguagem))

        elif escolha == "2":
            linguagem = input("Digite o nome da linguagem que deseja remover: ")

            if remover(linguagens, linguagem, linguagens_removidas):
                print("{} removido com sucesso.".format(linguagem))
            else:
                print("Não foi possível encontrar {} na lista".format(linguagem))
            
        elif escolha == "3":
            linguagem = input("Digite o nome da linguagem que deseja buscar: ")

            if buscar(linguagens, linguagem):
                print("A linguagem {} está cadastrada.".format(linguagem))
            else:
                print("A linguagem {} não está cadastrada.".format(linguagem))
        
        elif escolha == "4":
            if linguagens:
                print("Todas as linguagens cadastradas são: {}".format(linguagens))
            else:
                print("Nenhuma linguagem cadastrada.")

        elif escolha == "5":
            if linguagens_removidas:
                print("Linguagens removidas: ")
                for linguagem in linguagens_removidas:
                    print(linguagem)
            else:
                print("Nenhuma linguagem removida.")

        elif escolha == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida! Por favor, escolha entre 1 e 6.")

interface_usuario()
