sair = "s"

for _ in range(100): #O programa será repetido até 100 vezes, ou até o usuário decidir sair (break interrompe o loop).


    num1 = float(input("Digite o 1o valor: "))
    num2 = float(input("Digite o 2o valor: "))
    ope = input("Digite qual tipo de operação: ")
    continuar = input("Continuar a operação: (s = SAIR / c = CONTINUE): ") 

    if ope == "+":
             print(f"Resultado: {num1 + num2}")
    elif ope == "-":
            print(f"Resultado: {num1 - num2}")
    elif ope == "*":
            print(f"Resultado: {num1 * num2}")
    elif ope == "/":
            if num2 != 0:
                print(f"Resultado: {num1 / num2}")
    else:
            print("Erro! Divisão por zero não permitida.")
else: 
    print("Operação inválida.")
    
if continuar == "s":
        break
if continuar == "c":
     #fazer os if com as opçoes das operaçoes