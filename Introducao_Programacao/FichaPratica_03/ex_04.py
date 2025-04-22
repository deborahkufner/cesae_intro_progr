numero = int(input("Insira um número inteiro: "))


while numero <= 1:
    print(f"O número{numero} escolhido não é primo.")
else:
    divisor = 0

    for i in range(1, numero + 1):
        if numero % i == 0:
            divisor += 1
    if divisor == 2:
        print("O número é primo.")
    else:
        print("Não é primo.")