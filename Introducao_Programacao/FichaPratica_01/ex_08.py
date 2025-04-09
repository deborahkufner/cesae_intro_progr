nota1 = float(input("Digite a primeira nota (valor entre 0 e 10): "))
nota2 = float(input("Digite a segunda nota (valor entre 0 e 10): "))
nota3 = float(input("Digite a terceira nota (valor entre 0 e 10): "))

mponderada = ((nota1 * 25) + (nota2 * 35) + (nota3 * 40)) / (25 + 35 + 40)

if mponderada >= 9.5:
    print("PARABÉNS")
else:
    print("SENTA E CHORA")