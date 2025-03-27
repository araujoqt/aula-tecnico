import os
import time

os.system("cls || clear")

soma_notas = 0
contador = 0
media = 0

while True:
    nota = float(input("Digite uma nota: "))  
    soma_notas += nota  
    contador += 1  

    continuar = input("Deseja digitar mais uma nota? (S/N): ")
    if continuar == 'n':
        break  
   

media = soma_notas / contador

print(f"\nNotas inseridas: {contador}")
print(f"Média: {media:.2f}")
if media >= 7:
     print("Aprovado!")
elif 5 <= media < 7:
            print("Recuperação!")
else:
            print("Reprovado!")