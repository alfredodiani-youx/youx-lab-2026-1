from rich import print
from rich.panel import Panel

class Churrasco:
    def __init__(self, n, p):
        self.nome = n
        self.pessoas = p


    def analisar(self):
        kilos = self.pessoas * 0.4
        ta = Panel(f"Analisando [bold green]{self.nome}[/] com [bold blue]{self.pessoas} convidados[/]\nCada participante comerá 0.4Kg e cada Kg custará R$82.40 recomento comprar [bold purple on black]{kilos}Kg[/] de carne!\nO custo total será [bold red on black]R${kilos * 82.40:.2f}[/]\nCada pessoa pagará [bold yellow on black]R${(kilos * 82.40) / 15:.2f}[/]",title=self.nome)
        return ta

churras = Churrasco(input("Nome churrasco: "), int(input("Quantidade participantes: ")))
print(churras.analisar())