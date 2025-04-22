opcao = int(input("Escolha uma das opcoes: 1, 2, 3 ou 4: "))

for _ in range (1):

    if opcao == 1:
        print("Sua escolha foi CRIAR")
    elif opcao == 2:
        print("Sua escolha foi ATUALIZAR")
    elif opcao == 3:
        print("Sua escolha foi ELIMINAR")
    elif opcao == 4:
        print("Sua escolha foi SAIR")
        break
    else:
        print("Opção inválida")