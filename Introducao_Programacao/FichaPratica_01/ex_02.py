salario = float(input("Insira o salário: "))

imposto20 = salario * 0.2
imposto30 = salario * 0.3

if salario > 15000:
    print("Taxa a pagar (30%): ", imposto30)

elif salario < 15000:
    print("Taxa a pagar (20%): ", imposto20)