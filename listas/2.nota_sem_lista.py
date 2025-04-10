import os 

os.system("cls || clear")

soma = 0

for i in range(3):
    nota = float(input("Digite uma nota: "))
    soma += nota

media = soma / 3

print(f"Média: {media}")