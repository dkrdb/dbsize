import math

s = float(input("Digite o tamanho atual do banco de dados em GB: "))
r = float(input("Digite a taxa de crescimento mensal do banco de dados em %: "))
tamanho_maximo = float(input("Digite o tamanho máximo do banco de dados em GB: "))

t = math.log(tamanho_maximo/s) / math.log(1 + r/100)

anos = int(t / 12)
meses = int(t % 12)
semanas = int((t % 1) * 4)
dias = int(math.floor((t * 30) % 30))
horas = int(math.floor((((t * 30) % 30) % 1) * 24))
if horas == 24:
    dias += 1
    horas = 0
if dias > 30:
    meses += 1
    dias -= 30
minutos = int(math.floor(((((t * 30) % 30) % 1) * 24 - horas) * 60))

if anos == 0:
    if meses == 0:
        if semanas == 0:
            if dias == 0:
                print(f"O banco de dados levará {horas} horas e {minutos} minutos para atingir o tamanho máximo de {tamanho_maximo} GB.")
            else:
                print(f"O banco de dados levará {dias} dias, {horas} horas e {minutos} minutos para atingir o tamanho máximo de {tamanho_maximo} GB.")
        else:
            print(f"O banco de dados levará {semanas} semanas, {dias} dias, {horas} horas e {minutos} minutos para atingir o tamanho máximo de {tamanho_maximo} GB.")
    else:
        print(f"O banco de dados levará {meses} meses, {semanas} semanas, {dias} dias, {horas} horas e {minutos} minutos para atingir o tamanho máximo de {tamanho_maximo} GB.")
else:
    print(f"O banco de dados levará {anos} anos, {meses} meses, {semanas} semanas, {dias} dias, {horas} horas e {minutos} minutos para atingir o tamanho máximo de {tamanho_maximo} GB.")
