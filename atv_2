import os 

os.system("clear")

def verificar_voto(idade):
    if idade < 16:
        return "Não pode votar"
    elif 16 <= idade < 17:
        return "Voto opcional"
    elif 18 <= idade <= 65:
        return "Voto obrigatório"
    else:
        return "Voto opcional"

idade = int(input("Digite sua idade: "))

resultado = verificar_voto(idade)
print(f"O seu voto é: {resultado}")