import os 

os.system("clear")

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
nota3 = float(input('Terceira nota: '))

media = (nota1 + nota2 + nota3) / 3

print()
print('Media: ',media)

if media < 7:
    print('Situação: Reprovado')
else:
    print('Situação: Aprovado')