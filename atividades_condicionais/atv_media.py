import os 

os.system("clear")

n1 = int(input('Número um: '))
n2 = int(input('Número dois: '))

print()
media = (n1 + n2) / 2
soma = (n1 + n2) 
multi = (n1 * n2) 

print(f"Media: {media}")
print(f"Soma: {soma}")
print(f"Produto: {multi}")

maior_numero = max (n1,n2)
menor_numero = min (n1,n2)

print()
if n1< n2:
    print(f"Maior número é: {n2}")

elif n2< n1:
    print(f"Maior número é: {n1}")

if n1< n2:
    print(f"Menor número é: {n1}")

elif n2< n1:
    print(f"Menor número é: {n2}")

else:
    print("Os números são iguais")