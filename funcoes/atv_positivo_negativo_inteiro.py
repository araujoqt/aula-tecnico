import os 

os.system("cls || clear")

def positivo_negativo(num):
    if num > 0:
        print("Número positivo")
    elif num == 0:
        print("Número neutro")
    else:
        print("Negativo")

num = int(input("Digite um número inteiro: "))
positivo_negativo(num)