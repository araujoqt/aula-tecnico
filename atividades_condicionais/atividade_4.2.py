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

if n1 < n2:
    maior_numero = n2
    menor_numero = n1
else:
    maior_numero = n1
    menor_numero = n2

print()

if n1 == n2:
    print(f"Os números são iguais")
else:
    print(f"Maior número: {maior_numero}")
    print(f"Menor número: {menor_numero}")