from rich import print
from rich.panel import Panel

class churrasco:
    def __init__(self, titulo, quant):
        self.titulo = titulo
        self.quant = quant
    def __str__(self):
        return print(f'Analisando {self.titulo} com {self.quant} convidados!')
    def calcularCarne(self) -> float:
        return self.quant * 0.4
    def custoTotal(self) -> float:
        return self.calcularCarne() * 82.40
    def custoIndiv(self) -> float:
        return self.custoTotal()/self.quant
    def analisar(self):
        conteudo = f'Analisando {self.titulo} com {self.quant} convidados!'
        quantpessoa = self.quant * 0.4
        precocarne = quantpessoa * 82.40
        conteudo += f'\nCada participante comerá 0.4Kg e a carne está R$82.40/kg'
        conteudo += f'\nRecomendo comprar {self.calcularCarne():,.2f}Kg de carne'
        conteudo += f'\nO custo total será de R${self.custoTotal():,.2f}'
        conteudo += f'\nCada pessoa terá que pagar R${self.custoIndiv():.2f}'
        painel = Panel(conteudo, title=f'{self.titulo}')
        print(painel)

c1 = churrasco('Churras da Copa', 7)
c1.analisar()
# Consumo padrão: 400g p/ pessoa
# Preço: R$82,40/Kg