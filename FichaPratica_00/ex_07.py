#solicitar input - 3 valores

preco1 = float(input("Valor do primeiro produto: "))
preco2 = float(input("Valor do segundo produto: "))
preco3 = float(input("Valor do terceiro produto: "))

total = preco1 + preco2 + preco3

totalcomdesc = total * 0.9

print("Total da compra é de: ", totalcomdesc)