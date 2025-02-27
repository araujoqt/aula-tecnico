import os

os.system("clear")

opcao = int(input("Digite o número: "))

match opcao:
 case 1:
  mes = "Janeiro"
 case 2:
  mes = "Fevereiro"
 case 3:
  mes = "Março"
 case 4:
  mes = "Abril"
 case 5:
  mes = "Maio"
 case 6: 
  mes = "Junho" 
 case 7: 
  mes = "Julho"
 case 8: 
  mes = "Agosto"
 case 9: 
  mes = "Setembro"
 case 10: 
  mes = "Outubro"
 case 11: 
  mes = "Novembro"
 case 12: 
  mes = "Dezembro"
 case _: 
  mes = "Inválido."

print("")
print(f"Mês do ano: {mes}")