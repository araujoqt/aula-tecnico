import os 

os.system("clear")

quantidade_macas = int(input("Digite a quantidade de maçãs que deseja comprar: "))

if quantidade_macas < 12:
    preco_por_maca = 1.30
else:
    preco_por_maca = 1.00

valor_total = quantidade_macas * preco_por_maca

print(f"O valor total da sua compra é: R${valor_total:.2f}")