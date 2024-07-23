# a = int(input("Escolha um numero de 1 até 1000: "))
# b = 2

# while(b < a):
    
#     if a == 3 or a == 5:
#         print("Ele é um numero primo")
#         break
#     elif a % b == 0 or a % 3 == 0 or a % 5 == 0:
#         print("Não é primo")
#         break
#     else:
#         print("Ele é um numero primo")
        
#         break
        
# print("Fim do programa")


verificador = int(input("Digite um valor: "))

while(verificador > 2):
    verificador = int(input("Digite um valor"))

    if verificador == 2 or verificador == 3 or verificador == 5:
        print("Este número é primo")
    elif verificador % 2 == 0 or verificador % 3 == 0 or verificador % 5 == 0:
        print("Este número não é primo")
    else:
        print("Este número é primo ")