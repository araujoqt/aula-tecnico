import os
os.system("cls || clear")

def Metros(n1): 
    calculo = n1 * 10
    segundo_calculo = calculo * 10
    return segundo_calculo

n1 = int(input("Digite a quantidade de metros: "))

metro = Metros(n1)

print()
print(f"A quantidade de centimetros em metros foi de {metro}!")