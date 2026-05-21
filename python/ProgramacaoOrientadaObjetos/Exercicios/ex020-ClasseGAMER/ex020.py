from rich import print
from rich import inspect
from rich.panel import Panel

class gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favs = []
    def addFav(self, game):
        self.favs.append(game)
    def ficha(self):
        conteudo = f'Nome: {self.nome}'
        conteudo += f'\nJogos favoritos:'
        for game in enumerate(self.favs):
            conteudo += f'\n-> {game[1]}'
        painel = Panel(conteudo, title=f'Player {self.nick}', width=45)
        print(painel)


j1 = gamer('Artur', 'ThuurXD')
j1.addFav('Valorant')
j1.addFav('CS 2')
j1.addFav('Overwatch 2')
j1.addFav('Hollow Knight')
j1.addFav('Hollow Knight: Silksong')
j1.addFav('Bloons TD 6')
j1.addFav('PvZ Garden Warfare 2')
j1.ficha()