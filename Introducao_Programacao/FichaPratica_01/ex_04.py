posicao = int(input("Digite a colocacao: "))

pontos = 0

if posicao == 1:
    pontos = 10
elif posicao == 2:
    pontos = 8
elif posicao == 3:
    pontos = 6
elif posicao == 4:
    pontos = 5
elif posicao == 5:
    pontos = 4
elif posicao == 6:
    pontos = 3
elif posicao == 7:
    pontos = 2
elif posicao == 8:
    pontos = 1
else:
    pontos = 0

print("A pontuação é: ", pontos)