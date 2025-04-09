valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

valor1, valor2 = valor2, valor1

#usando uma var extra
vtemporaria = valor1
valor2 = valor2
valor2 = vtemporaria

print("O resultado do valor1 é:", valor1)
print("O resultado do valor2 é:", valor2)