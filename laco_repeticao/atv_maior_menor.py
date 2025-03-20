import os 

os.system("cls || clear")

quantidade_notas = 2
soma = 0

for i in range(quantidade_notas):
    while True:
        nota = float(input(f"Digite a {i+1} nota: "))

        if nota < 0 or nota > 10:
            print("Nota inválida. \n")
        
        else:
            soma += nota
            break

media = soma / quantidade_notas

print(f"Média: {media}")