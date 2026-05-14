from rich import print
from rich.table import Table
class Produto:
    def __init__(self, produto, valor):
        self.nome = produto
        self.valor = valor

    def etiqueta(self):
        et = Table(title="Produto")
        et.add_column("Nome")
        et.add_column("Valor")
        et.add_row(self.nome, f"R$ {self.valor}")
        return et

pao = Produto("Pão de queijo", 22.00)
print(pao.etiqueta())