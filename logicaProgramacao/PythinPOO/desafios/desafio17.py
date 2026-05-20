from rich import print
from rich.table import Table

class Produto:
    def __init__(self, produto, preco):
        self.produto = produto
        self.preco = preco

    def etiquera(self):
        etiqueta = Table(title='Produto')
        etiqueta.add_column(f'{self.produto}', justify= 'center')
        etiqueta.add_row(f'R${self.preco:,}')
        print(etiqueta)

produto1 = Produto('Iphone 17 Pro Max',25000)
produto2 = Produto('Notebook Gamer', 8000)
produto1.etiquera()
produto2.etiquera()