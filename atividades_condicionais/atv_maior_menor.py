import os 

os.system("clear")


# Solicitando dados para o usuário.
primeiro_n = int(input("Digite o primeiro número:"))
segundo_n = int(input("Digite o segundo número:"))

# Verificando o maior número/menor número.
if primeiro_n > segundo_n:
    maior = primeiro_n
    menor = segundo_n
else:
    maior = primeiro_n
    menor = segundo_n

# Exibindo dados.
print()
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")