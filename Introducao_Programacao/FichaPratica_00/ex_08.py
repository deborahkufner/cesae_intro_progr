#input das musicas

faixa1_min, faixa1_seg = int(input("Faixa 1 - Minutos ")), int(input("Faixa 1 - Segundos: "))
faixa2_min, faixa2_seg = int(input("Faixa 2 - Minutos: ")), int(input("Faixa 2 - Segundos: "))
faixa3_min, faixa3_seg = int(input("Faixa 3 - Minutos: ")), int(input("Faixa 3 - Segundos: "))
faixa4_min, faixa4_seg = int(input("Faixa 4 - Minutos: ")), int(input("Faixa 4 - Segundos: "))
faixa5_min, faixa5_seg = int(input("Faixa 5 - Minutos: ")), int(input("Faixa 5 - Segundos: "))

totalsegundos = 0

totalminutos = faixa1_min + faixa2_min + faixa3_min + faixa4_min + faixa5_min

somasegundos = faixa1_seg + faixa2_seg + faixa3_seg + faixa4_seg + faixa5_seg

#converter p segundos
totalsegundos += (totalminutos * 60) + somasegundos

#calcular seg, min e horas
horas = totalsegundos // 3600
minutos = (totalsegundos % 3600) // 60
segundos = totalsegundos % 60

print(f"tempo total = {horas}:{minutos}:{segundos}")



