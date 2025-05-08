import os

os.system("cls || clear")

valores = [0] * 5

for i in range(5):
    numero = int(input(f"Digite o {i+1}º número: "))

    if numero >= 0:
        valores[i] = numero
    else:
        print("Valor negativo. Será armazenado como 0.")

print()
print("Valores armazenados no vetor:")
for i in range(5):
    print(f"Posição {i}: {valores[i]}")
