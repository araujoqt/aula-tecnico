import os 

os.system("clear")

primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))
operacao = input("Digite o operador: ")

match operacao:
    case "+":
        resultado = primeiro_numero + segundo_numero
    case "-":
        resultado = primeiro_numero - segundo_numero
    case "*":
        resultado = primeiro_numero * segundo_numero
    case "/":
        resultado = primeiro_numero / segundo_numero
    case _:
        resultado = 0
        print("Você está fazendo algo de errado, tente novamente!")

print()
print(f"Primeiro número: {primeiro_numero}")
print(f"Segundo número: {segundo_numero}")
print(f"Operação: {operacao}")
print(f"Resultado: {resultado}")