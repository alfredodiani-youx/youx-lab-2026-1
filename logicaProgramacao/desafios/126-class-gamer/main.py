from rich import print
from rich.panel import Panel

class Gamer:
    def __init__(self,n , ni):
        self.nome = n
        self.nick = ni
        self.jogos = []

    def add_favoritos(self, jogo):
        self.jogos.append(jogo)
    def fichak(self):
        conteudo = f"Nome real = [bold blue on white]{self.nome}[/]"
        conteudo += f"\nNick = {self.nick}"
        conteudo += f"\nJogos favoritos: \n"
        for i in self.jogos:
            conteudo += f"[bold green on black]{i}[/]\n"
        self.ficha = Panel(conteudo, title=self.nick)
        print(self.ficha)

jo = Gamer("Joao", "035.neto")
jo.add_favoritos("sonic")
jo.add_favoritos("joo")
jo.fichak()