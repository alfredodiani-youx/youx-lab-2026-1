from rich import print
import rich

class caneta:
    def __init__(self, cor = "azul"):
        escolha = ""
        match cor.lower().strip():
            case "azul":
                escolha = "[blue]"
            case "vermelho" | "vermelha":
                escolha = "[red]"
            case "roxo" | "roxa":
                escolha = "[magenta]"
            case _:
                escolha = "[white]"
        self.cor = escolha
        self.tampada = True
    def escrever(self, msg):
        if self.tampada:
            print(f'A {self.cor}caneta[/] está tampada!')
        else:
            print(f'{self.cor}{msg}[/]', end='')
    def quebrarLinha(self, qtd = 1):
        print(f'\n' * qtd, end='')
    def tampar(self):
        self.tampada = True
    def destamp(self):
        self.tampada = False


c1 = caneta("azul")
c2 = caneta("vermelha")
c3 = caneta("roxo")
c1.destamp()
c2.destamp()
c3.destamp()
c1.escrever("Opaa, blz? ")
c1.quebrarLinha(1)
c2.escrever("Eai cara! ")
c3.escrever("Vamos codar!")