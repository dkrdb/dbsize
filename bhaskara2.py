import math

tamanho_atual = float(input("Digite o tamanho atual do banco de dados em GB: "))
taxa_crescimento = float(input("Digite a taxa de crescimento mensal do banco de dados em %: "))
tamanho_maximo = float(input("Digite o tamanho máximo do banco de dados em GB: "))

taxa_crescimento_decimal = taxa_crescimento / 100
a = 1 - taxa_crescimento_decimal
b = tamanho_atual * taxa_crescimento_decimal
c = - tamanho_maximo

delta = b ** 2 - 4 * a * c

if delta < 0:
    print("Não há raízes reais.")
else:
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    raiz2 = (-b - math.sqrt(delta)) / (2 * a)

    if raiz1 < 0:
        anos = 0
        meses = 0
        semanas = 0
        dias = 0
        horas = 0
        minutos = 0
    else:
        total_minutos = raiz1 * 30.44 * 24 * 60
        anos = int(total_minutos / (365 * 24 * 60))
        total_minutos -= anos * 365 * 24 * 60
        meses = int(total_minutos / (30 * 24 * 60))
        total_minutos -= meses * 30 * 24 * 60
        semanas = int(total_minutos / (7 * 24 * 60))
        total_minutos -= semanas * 7 * 24 * 60
        dias = int(total_minutos / (24 * 60))
        total_minutos -= dias * 24 * 60
        horas = int(total_minutos / 60)
        total_minutos -= horas * 60
        minutos = int(total_minutos)

    print(f"O banco de dados levará {anos} anos, {meses} meses, {semanas} semanas, {dias} dias, {horas} horas e {minutos} minutos para atingir o tamanho máximo de {tamanho_maximo} GB.")
