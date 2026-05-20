from rich.panel import Panel
from rich import print

class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = []
    def add_favoritos(self, jogos):
        self.favoritos.append(jogos)
        sorted(self.favoritos)
    def ficha(self):
        conteudo = f'\nNome real: {self.nome}'
        conteudo += '\nJogos favoritos:'
        for numero, jogo in enumerate(self.favoritos):
            conteudo += f'\n{jogo}'
        ficha = Panel(f'{conteudo}', title=f'Jogador <{self.nick}>')
        print(ficha)
jogador = Gamer('Fabrico da Silva', 'detonator2025')
jogador.add_favoritos('Mario bros')
jogador.add_favoritos('Sonic')
jogador.add_favoritos('God of War')
jogador.add_favoritos('Fortnite')
jogador.ficha()