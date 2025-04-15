inicio = int(input("Insira o primeiro numero: "))
fim = int(input("Insira o segundo numero: "))

contador = inicio
print("Os numeros multiplos de 5 são:")

while contador <= fim:
    if contador % 5 == 0:
        print(contador)
    contador += 1