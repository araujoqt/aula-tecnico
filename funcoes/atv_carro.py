import os
from dataclasses import dataclass

# Limpa o terminal
os.system("clear || cls")

@dataclass
class Carros:
    marca: str
    modelo: str
    categoria: str
    preco: str

lista_carros = []
QUANTIDADE_CARROS = 2

print("Informe os dados dos carros:")
print()

for i in range(QUANTIDADE_CARROS):
    carro = Carros(
        marca=input("Marca: "),
        modelo=input("Modelo: "),
        categoria=input("Categoria: "),
        preco=input("Preço: ")
    )
    lista_carros.append(carro)

print("\n= Exibindo dados dos carros =")
for carro in lista_carros:
    print(f"\nMarca: {carro.marca}")
    print(f"Modelo: {carro.modelo}")
    print(f"Categoria: {carro.categoria}")
    print(f"Preço: {carro.preco}")

print("\n= Salvando os dados =")
nome_arquivo = "carros.txt"

with open(nome_arquivo, "a") as arquivo:
    for carro in lista_carros:
        arquivo.write(f"{carro.marca}, {carro.modelo}, {carro.categoria}, {carro.preco}\n")

print("\nSalvo com sucesso!")
