numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

median = (numero1 + numero2 + numero3) / 3
mponderada = ((numero1 * 20) + (numero2 * 30) + (numero3 * 50)) / (20 + 30 + 50)

print("A média dos valores é:", median)
print("A média ponderada é:", mponderada)