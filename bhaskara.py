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
    else:
        meses = int(raiz1)
        resto_meses = raiz1 - meses
        dias = int(resto_meses * 30.44)
        semanas = int(dias / 7)
        dias = dias % 7
        anos = int(meses / 12)
        meses = meses % 12

        print("O banco de dados levará", anos, "anos,", meses, "meses,", semanas, "semanas e", dias, "dias para atingir o tamanho máximo de", tamanho_maximo, "GB.")
