saldo1 = float(input("Digite seu saldo: "))
vmov = float(input("Qual vamos deseja movimentar? "))

saldoatual = saldo1 + vmov

if saldoatual > 0:
    print("Saldo: ",saldo1,"\n","Valor movimentado: ",vmov,"\n","Saldo Atual: ",saldoatual)

else:
    print("Operação Inválida. Saldo insuficiente", saldo1, "\n", "Saldo atual: ", saldo1)
