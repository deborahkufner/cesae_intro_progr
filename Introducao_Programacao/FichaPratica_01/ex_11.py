saldoinicial = float(input("Digite seu saldo inicial: "))
vmov = float(input("Qual vamos deseja movimentar? "))

saldoatual = saldoinicial + vmov

if saldoatual >= 0:
    print("Saldo atual: ",saldoatual)

else:
    print("Operação Inválida. Saldo insuficiente", saldoinicial, "->", saldoatual)