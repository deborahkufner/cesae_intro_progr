numero = int(input("Digite um numero inteiro nao negativo: "))

fatorial = 1
contador = numero

while contador > 0:
    fatorial *= contador
    contador -= 1
print("O fatorial de", numero, "é = ", fatorial)