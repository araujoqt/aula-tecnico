import os
from dataclasses import dataclass


os.system("cls" if os.name == "nt" else "clear")


@dataclass
class Carro:
    marca: str
    modelo: str
    categoria: str
    preco: float


lista_carros = []


print("Informe os dados dos carros:")
for i in range(2):
    print(f"\nCarro {i+1}:")
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    categoria = input("Categoria: ")
    preco = float(input("Preço: "))

    carro = Carro(marca, modelo, categoria, preco)
    lista_carros.append(carro)


print("\n= Exibindo dados dos carros =")
for carro in lista_carros:
    print(f"Marca: {carro.marca}")
    print(f"Modelo: {carro.modelo}")
    print(f"Categoria: {carro.categoria}")
    print(f"Preço: R$ {carro.preco:.2f}")
    print("-" * 30)


nome_arquivo = "dados_carros.txt"
print("\n= Salvando os dados dos carros =")

with open(nome_arquivo, "a", encoding="utf-8") as arquivo:
    for carro in lista_carros:
        arquivo.write(f"{carro.marca}, {carro.modelo}, {carro.categoria}, {carro.preco:.2f}\n")

print("\nSalvo com sucesso!")