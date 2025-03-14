import os 

os.system("cls || clear")

soma = 0

for i in range(4):  
    n1 = int(input(f"Digite a {i+1}° nota: "))
    soma += n1

media = soma / 4     

print()
print(f"Média: {media}")  