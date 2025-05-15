import os
from dataclasses import dataclass

os.system("cls" if os.name == "nt" else "clear")

@dataclass
class Funcionario:
    nome: str
    data_admissao: str
    matricula: str
    endereco: str

@dataclass
class Cliente:
    nome: str
    nascimento: str
    endereco: str

def salvar_funcionarios(lista):
    nome_arquivo = "dados_funcionarios.csv"

    with open(nome_arquivo, "a") as arquivo_funcionarios:
        for funcionario in lista:
            arquivo_funcionarios.write(f"{funcionario.nome}, {funcionario.data_admissao}, {funcionario.matricula}, {funcionario.endereco}\n")

    print("Dados dos funcionários salvos com sucesso.")

def salvar_clientes(lista):
    nome_arquivo = "dados_clientes.csv"

    with open(nome_arquivo, "a") as arquivo_clientes:
        for clientes in lista:
            arquivo_clientes.write(f"{clientes.nome}, {clientes.nascimento}, {clientes.endereco}\n")

    print("Dados dos clientes salvos com sucesso.")

lista_funcionarios = []
lista_clientes = []

for i in range(1):
    print("Digite os dados do funcionário: ")
    funcionario = Funcionario(
        nome= input("Nome: "),
        data_admissao=input("Data de admissão: "),
        matricula=input("Matrícula: "),
        endereco=input("Endereço: ")
    )
    lista_funcionarios.append(funcionario)
    print()

    print("Digite os dados do cliente: ")
    cliente = Cliente(
        nome=input("Nome: "),
        nascimento=input("Data de nascimento: "),
        endereco=input("Endereço: ")
    )
    lista_clientes.append(cliente)
    print()

salvar_funcionarios(lista_funcionarios)
salvar_clientes(lista_clientes)