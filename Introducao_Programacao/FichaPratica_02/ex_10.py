numLimite = int(input("Insira o limite: "))
salto = int(input("Insira o numero salto: " ))

#conidcao

if numLimite > 0 and salto > 0:
    contador = 0
    while contador <= numLimite:
        print(contador)
        contador += salto #contador = contador + salto