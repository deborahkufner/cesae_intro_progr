salario = float(input("Insira o salário: "))


if salario <= 15000:
    imposto20 = salario * 0.2
    print("Taxa a pagar (20%): ", imposto20)

elif salario >= 15000 and salario <=20000:
    imposto30 = salario * 0.3
    print("Taxa a pagar (30%): ", imposto30)

elif salario > 20000 and salario <= 25000:
    imposto35 = salario * 0.35
    print("Taxa a pagar (35%): ", imposto35)

else: 
     imposto40 = salario * 0.40
     print("Taxa a pagar (40%): ", imposto40)