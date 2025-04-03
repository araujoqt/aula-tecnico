import os 

os.system("cls || clear")

def par_impar(num):
    if num % 2 == 0:
        print(f"{num} é par")
    else:
        print(f"{num} é ímpar")

num = int(input("Digite um número: "))
par_impar(num)