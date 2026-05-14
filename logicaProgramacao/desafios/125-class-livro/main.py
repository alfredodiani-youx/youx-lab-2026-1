from rich import print
from rich.emoji import Emoji

class Livro:
    def __init__(self, t, p):
        self.titulo = t
        self.pag = p
        self.atual = 0
        self.restante = self.pag - self.atual
    def avancar(self, pags=0):
        if pags <= self.restante:
            self.atual += pags
            self.restante = self.pag - self.atual
            if self.atual == 0:
                return f":book: Você acabou de abrir o livro [bold green]'{self.titulo}'[/] que possui {self.pag} páginas no total."
            elif self.atual == self.pag:
                return f":book: você está na [bold red]última pagina do livro[/]"
            else:
                return f":book: você está na [bold blue]{self.atual}° página[/], ainda faltam [bold red]{self.restante} páginas[/]"
        else:
            return f"[bold green]Parabéns!!!![/] Você finalizou o livro!"

livro = Livro(input("Nome livro: "), int(input("Paginas: ")))
o = input("Deseja abrir o livro?: ").strip()[0]
print(livro.avancar())
while o not in "Nn" and livro.restante >= 1:
    print(livro.avancar(int(input("Deseja pular quantas páginas?: "))))
    o = input("Deseja continuar?: ").strip()[0]
print(livro.avancar(10))