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
maior_idade = 0
menor_idade = 100

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
            idade = int(input("Digite a sua idade: "))
            salario = float(input("Digite o salário da pessoa: "))
            genero = input("Digite o genêro (F/M): ")
        case 2:
            print("Você escolheu: Exibir resultados")
            print(f"Nome: {nome}") 
            print(f"I: {nome}") 
            print(f"Nome: {nome}") 
            print(f"Nome: {nome}") 
        case 3:
            print("Você escolheu: Sair")
        case _:
            print("Opção inválida. \nTente novamente... \n")
            
total_salario += salario
total_idade += idade
contador_pessoas += 1 

if idade > maior_idade:
    maior_idade = idade
if idade < menor_idade:
    menor_idade = idade