sair = "s"

for _ in range(100):


    num1 = float(input("Digite o 1o valor: "))
    num2 = float(input("Digite o 2o valor: "))
    ope = input("Digite qual tipo de operação: ")
    continuar = input("Continuar a operação: (s = SAIR / c = CONTINUE)") 

    if continuar == "s":
        break
    if continuar == "c":
        #fazer os if com as opçoes das operaçoes...