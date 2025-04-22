

jogador1 = int(input("Digite um número entre 0 e 100: "))
tentativa = 0

for _ in range (10):
    tentativa += 1
    jogador2 = int(input("Adivinhe o número: "))
    if jogador2 > jogador1:
        print("O numero que escolheu é maior.")
    elif jogador2 < jogador1:
        print("O numero que escolheu é menor.")
    else: 
        print("Parabéns!Vocè acertou em", tentativa, "tentativas! O número secreto é: ", jogador2)
        break