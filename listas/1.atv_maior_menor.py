import os 

os.system("cls || clear")

numeros = [] 

for i in range(5):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

maior = max(numeros)
menor = min(numeros)

print(f"\nMaior número: {maior}")
print(f"Menor número: {menor}")