num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
ope = input("Digite uma das seguintes operações aritméticas: +, -, * ou /: ")


soma = num1 + num2
subt = num1 - num2
multipl = num1 * num2
divis = num1 / num2

if ope == "+": 
    print(soma)
elif ope == "-":
    print(subt)
elif ope == "*":
    print(multipl)
elif ope == "/":
    print(divis)
else:
    print("ERRO")