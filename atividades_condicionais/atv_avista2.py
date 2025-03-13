import os 

os.system("clear")

valor_produto = float(input("Digite o valor do produto: "))

forma_de_pagamento = int(input("Digite a forma de pagamento: "))

match forma_de_pagamento:
    case 1:
        desconto = valor_produto * 0.10
        valor_com_desconto = valor_produto - desconto

        print(f"Valor do produto: {valor_produto}")
        print(f"Forma de pagamento: à vista")
        print(f"Valor do desconto: {desconto}")
        print(f"Total a pagar: {valor_com_desconto}")

    case 2:
        quantidade_parcelas = int(input("Digite a quantidade de parcelas: "))
        if quantidade_parcelas >= 1 or quantidade_parcelas <= 6:
            print("Opção inválida")
            valor_da_parcela = valor_produto / quantidade_parcelas
        
        print(f"Valor do desconto: {valor_produto}")
        print(f"Forma de pagamento: à prazo")
        print(f"Quantidade de parcelas: {quantidade_parcelas}")
        print(f"Valor por parcela: {valor_da_parcela}")
        print(f"Total à prazo: {valor_da_parcela}")

    case _:
        print("Opção inválida")