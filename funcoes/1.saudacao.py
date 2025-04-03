import os 

os.system("cls || clear")

def saudacao(nome, nome_disciplina):
    print(f"Olá {nome}! Bem-vindo ao curso de DS!")

def disciplina(nome):
    print(f"A disciplina {nome_disciplina} faz parte do curso de DS!")

nome = input("Digite seu nome: ")
nome_disciplina = input("Digite o nome da disciplina: ")

saudacao(nome)
disciplina(nome_disciplina)