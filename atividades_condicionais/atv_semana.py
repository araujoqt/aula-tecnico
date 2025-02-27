import os

os.system("clear")

opcao = int(input("Digite o número: "))

match opcao:
 case 1:
  semana = "Segunda-feira"
  resultado = "Dia útil"
 case 2:
  semana = "Terça-feira"
  resultado = "Dia útil"
 case 3:
  semana = "Quarta-feira"
  resultado = "Dia útil"
 case 4:
  semana = "Quinta-feira"
  resultado = "Dia útil"
 case 5:
  semana = "Sexta-feira"
  resultado = "Dia útil"
 case 6: 
  semana = "Sábado" 
  resultado = "Não útil"
 case 7: 
  semana = "Domingo"
  resultado = "Não Util"
 case _: 
  semana = "Inválido"

print("")
print(f"Dia da semana: {semana}")
print(f"Resultado: {resultado}")