import os 

# Limpa o terminal.
os.system("clear")

# Solicitando dados (Entrada)
idade = int(input("Digite sua idade:"))

# Verificando (Processamento)
if idade < 18:
    print("Acesso negado!")
else:
     print("Acesso permitido!")