import os 

os.system("clear")

# Solicitando dados para o usuário.
primeiro_n = int(input("Insira o primeiro número: "))
segundo_n = int(input("Insira o segundo número: "))
terceiro_n = int(input("Insira o terceiro número: "))

# Verificando o maior número/menor número.
maior_numero = max (primeiro_n, segundo_n, terceiro_n)
menor_numero = min (primeiro_n, segundo_n, terceiro_n)

# Exibindo dados.
print()
print(f"Primeiro número: {primeiro_n}")
print(f"Segundo número: {segundo_n}")
print(f"Terceiro número: {terceiro_n}")
print()
print(f"Maior número: {maior_numero}")
print(f"Menor número: {menor_numero}")