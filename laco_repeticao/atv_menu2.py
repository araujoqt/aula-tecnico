import os

os.system("cls || clear")

nome = ""
idade = 0 
salario = 0.0
genero = ""
total_salario = 0.0
total_idade = 0
mulheres_salario_alto = 0
contador_pessoas = 0
maior_idade = None
menor_idade = None

while True:
    print("""
    ================= MENU =================
    1 | Adicionar pessoa 
    2 | Exibir resultados 
    3 | Sair
    """)
    
    opcao = int(input("Digite o número da opção desejada: "))

    print()
    match opcao:
            case 1:
                print("Você escolheu: Adicionar pessoa")
                nome = input("Digite o nome da pessoa: ")
                idade = int(input("Digite a idade da pessoa: "))
                salario = float(input("Digite o salário da pessoa: "))
                genero = input("Digite o genêro (F/M): ")
            case 2:
                if contador_pessoas > 0:
                    media_salario = total_salario / contador_pessoas
                    print("Você escolheu: Exibir resultados")
                    print()
                print(f"Nome: {nome}")
                print(f"Idade: {idade}") 
                print(f"Salario: {salario}") 
                print(f"Gênero: {genero}") 
                print(f"Média de salário: R$ {media_salario:.2f}") 
                print(f"Maior idade: {maior_idade}") 
                print(f"Menor idade: {menor_idade}") 
                print(f"Quantidade de mulheres com salário maior ou igual a 5000: {mulheres_salario_alto}")
            case 3:
                print("Você escolheu: Sair")
                break
            case _:
                print("Opção inválida. \nTente novamente... \n")
                
    total_salario += salario
    total_idade += idade
    contador_pessoas += 1 

    if maior_idade is None or idade > maior_idade:
            maior_idade = idade
    if menor_idade is None or idade < menor_idade:
            menor_idade = idade
        

    if genero == 'F' and salario >= 5000:
     mulheres_salario_alto += 1
    print(f"{nome} foi adicionada com sucesso!")