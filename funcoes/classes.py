import os 
from dataclasses import dataclass
os.system("clear || cls")

@dataclass
class pessoa:
    nome: str
    email: str
    endereco: endereco
    