import os 

os.system("cls || clear")
numero = int(input("Digite um número: "))


for i in range(1, 21):  
    resultado = numero * i 
    print(f"{numero} x {i} = {resultado}")  