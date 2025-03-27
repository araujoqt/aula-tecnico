import os
import time

os.system("cls || clear")

soma = 0
contador = 0

while True:
    numero = int(input("Digite um número inteiro positivo: "))
    
    if numero < 0:
        break
    
    soma += numero
    contador += 1

    if contador > 0:
        media = soma / contador
        print(f"A média aritmética dos números informados é: {media}")
    else:
        print("Nenhum número positivo foi informado.")
