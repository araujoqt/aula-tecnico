import os 

os.system("clear")

dia = int(input("Digite o número da semana: "))

match dia: 
    case 1 | 7:
        resultado = "Fim de semana"
    case 2 | 3 | 4 | 5 | 6:
        resultado = "Dia útil"
    case _:
        resultado = "Opção inválida"
    
print()
print(f"Resultado: {resultado}")