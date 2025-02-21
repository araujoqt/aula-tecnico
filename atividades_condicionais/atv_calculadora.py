import os 

os.system("clear")

print("Calculadora SENAI")
numero_um = float(input("Digite o primeiro número: "))
numero_dois = float(input("Digite o segundo número: "))

print()
operador = input("Digite o operador: ")

if operador == "+":
    resultado = numero_um + numero_dois
elif operador == "-":
    resultado = numero_um - numero_dois
elif operador == "*":
    resultado = numero_um * numero_dois
elif operador == "/":
    if numero_dois != 0:
        resultado = numero_um / numero_dois
else:
    resultado = "Você está fazendo algo de errado, tente novamente!"

print()
print(f"Primeiro número: {numero_um} ")
print(f"Segundo número: {numero_dois}")
print(f"Operador: {operador}")
print(f"Resultado: {resultado}")