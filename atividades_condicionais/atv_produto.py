import os 

os.system("clear")

n1 = float(input('Número um: '))
n2 = float(input('Número dois: '))

print()
media = (n1 + n2) / 2
soma = (n1 + n2) 
multi = (n1 * n2) 

maior_numero = max (n1,n2)
menor_numero = min (n1,n2)

print(f"Soma: {soma}")
print(f"Produto: {multi}")
print(f"Média: {media}")
print()
print(f"Maior número: {maior_numero}")
print(f"Menor número: {menor_numero}")