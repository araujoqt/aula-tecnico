import os 

os.system("cls || clear")

soma = 0

for i in range(5):  
    numero = int(input(f"Digite o {i+1}° número inteiro: "))
    soma += numero

print()
print(f"Soma: {soma}")  