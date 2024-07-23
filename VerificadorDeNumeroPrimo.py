
verificador = int(input("Digite um valor: "))

while(verificador > 2):
    verificador = int(input("Digite um valor"))

    if verificador == 2 or verificador == 3 or verificador == 5:
        print("Este número é primo")
    elif verificador % 2 == 0 or verificador % 3 == 0 or verificador % 5 == 0:
        print("Este número não é primo")
    else:
        print("Este número é primo ")