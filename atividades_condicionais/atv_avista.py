import os

os.system("clear")

valor = float(input("Digite o valor do produto: "))

print("""
=========== FORMA DE PAGAMENTO =========== 
1    \tDébito
2    \tCrédito

""")
forma_de_pagamento = int(input("Digite a forma de pagamento: "))

match forma_de_pagamento:
    case 1:
        desconto = valor * 0.10
        total = valor - desconto
        print()
        print(f"Valor: {valor}")
        print(f"Forma de pagamento: {forma_de_pagamento}")
        print(f"Valor do desconto: {desconto}")
        print(f"Total: {total}")
    case 2:
        print("Você pode parcelar em até 6x sem juros.")
        parcelas = int(input("Digite a quantidade de parcelas: "))
        if parcelas >= 1 and parcelas < 6:
            valor_parcelado = (valor / parcelas)

        print() 
        print(f"Valor: {valor}")
        print(f"Parcelas: {parcelas}")
        print(f"Valor parcelado: {valor_parcelado}")
        print(f"Forma de pagamento: {forma_de_pagamento}")
        print(f"Total: {total}")
    case _:
        print("Opção inválida")

print()
print(f"Desconto: {desconto}")