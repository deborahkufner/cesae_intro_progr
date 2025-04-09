hora = int(input("Insira a hora: "))
minuto = int(input("Insira o minuto: "))

novahora = hora - 12

if hora < 12:
    print(hora,":",minuto, "AM")

elif hora > 12:
    print(novahora,":",minuto, "PM")