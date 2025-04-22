quantidade = int(input("Quantos numeros deseja inserir?"))

contador = 1

anterior = None 
crescente = True

while contador <= quantidade:
    numero = int(input("Digite um numero: "))
    
    if anterior is not None and numero < anterior:
        crescente = False

    anterior = numero
    contador += 1

if crescente:
    print("A ordem está em ordem crescente!")
else:
    print("A sequencia não esta em ordem crescente.")
    
