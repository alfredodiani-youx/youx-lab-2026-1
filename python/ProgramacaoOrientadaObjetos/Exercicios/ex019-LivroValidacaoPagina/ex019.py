from rich import print
import time
class livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.totpaginas = paginas
        self.pagatual = 1
        print(f'Você acabou de abrir  o livro "{self.titulo}", que tem {self.totpaginas} páginas no total.\nVocé agora está na página {self.pagatual}')
    def avancarpag(self, quantid = 1):
        cont = 0
        for pag in range(0, quantid, 1):
            if not self.fimDoLivro():
                self.pagatual += 1
                print(f'Pág{self.pagatual} -> ', end='')
                time.sleep(0.2)
                cont += 1
        print(f'\nVocé avançou {cont} páginas e agora está na Página {self.pagatual}')
        if self.fimDoLivro():
            print(f'Você chegou ao final do livro "{self.titulo}"')
    def fimDoLivro(self) -> bool:
        if self.pagatual == self.totpaginas:
            return True
        else:
            return False


l1 = livro('Jujutsu Kaisen Vol.132', 192)
l1.avancarpag(10)