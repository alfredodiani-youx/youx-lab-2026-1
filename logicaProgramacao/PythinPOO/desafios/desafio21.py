from rich import print
class Caneta:
    def __init__(self, cor):
        self.cor = cor
    def destampar(self):
        self.destampar = True
    def escrever(self, msg):
        if self.destampar != True:
            print('A caneta está tampada.')
        elif self.cor == 'azul':
            print(f'[blue]{msg}[/]')
        elif self.cor == 'vermelha':
            print(f'[red]{msg}[/]')
        elif self.cor == 'verde':
            print(f'[green]{msg}[/]')

c1 = Caneta('azul')
c1.destampar()
c1.escrever('Olá! Mundo.')

c2 = Caneta('vermelha')
c2.destampar()
c2.escrever('Olá! Mundo.')

c3 = Caneta('verde')
c3.destampar()
c3.escrever('Olá! Mundo.')