import os 

os.system("cls || clear")

notas = [] 

for i in range(3):
    nota = float(input("Digite uma nota: "))
    notas.append(nota)

soma = sum(notas)
media = soma / 3

for nota in notas:
    print(f"Nota: {nota}")

print(f"Média: {media}")