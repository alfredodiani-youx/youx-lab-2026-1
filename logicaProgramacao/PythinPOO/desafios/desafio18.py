from rich import print
from rich.panel import Panel

class Churrasco:
    def __init__(self, titulo, quantidade):
        self.titulo = titulo
        self.quantidade = quantidade
        self.recomendacao = 0.4 * quantidade
        self.custo = self.recomendacao * 82.40
        self.pessoa = self.custo / quantidade
    def analisar(self):
        analise = Panel(f'''Analisando {self.titulo} com {self.quantidade}
Cada participante comerá 0.4Kg de carne e cada Kg de carne custa R$82.40
Recomendo comprar {self.recomendacao}Kg de carne
O custo total sera de R${self.custo:.2f}
Cada pessoa pagará R${self.pessoa:.2f} para participar''', title=self.titulo)
        print(analise)

churrasco = Churrasco('Churras dos amigos', 22)
churrasco.analisar()