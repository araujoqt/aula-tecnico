import os 

# Limpa o terminal.
os.system("clear")

# Solicitando dados (Entrada)
idade = int(input("Digite sua idade:"))

# Verificando (Processamento)
if idade < 18:
    print("Acesso negado!")

if idade > 18:
    print("Acesso permitido!")

# Exibindo dados (Saída)
print()
print(f"Idade: {idade}")