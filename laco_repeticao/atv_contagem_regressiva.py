import os 
import time

os.system("cls || clear")
numero = int(input("Digite um número: "))

print()
print("CONTAGEM REGRESSIVA")
for i in range(numero,0,-1):
    print(f"Número: {i}")
    time.sleep(0.5)

print()
print("ACABOU")