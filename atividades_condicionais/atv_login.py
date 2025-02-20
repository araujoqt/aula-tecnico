import os 

os.system("clear")

login_cadastrado = "araujo@"
senha_cadastrada = "1234"

login = input("Digite seu login: ")
senha = input("Digite sua senha: ")

if login_cadastrado == login and senha_cadastrada == senha:
    print("Seja bem vindo")
else:
    print("Login ou senha inválidos")
