import os 

os.system("clear")
idade = int(input("Digite sua idade: "))


# Opção 1
if idade < 18 or idade > 65:
    print("Não é obrigado a votar")
else:
    print("É obrigado a votar")

# Opção 2
if idade >= 18 and idade <=65:
    print("É obrigado a votar")
else:
    print("Não é obrigado a votar")