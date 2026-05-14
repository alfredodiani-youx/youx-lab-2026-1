from rich import print
class Caneta:
    def __init__(self, nome):
        if nome.lower() == "azul":
            self.cor = "blue"
        if nome.lower() == "vermelha":
            self.cor = "red"
        if nome.lower() == "verde":
            self.cor = "green"
        elif not self.cor:
            print("Erro: cor invalida! cores disponiveis: azul, vermelha, verde")
        self.tampada = True

    def destampar(self):
        self.tampada = False
    def escrever(self, texto):
        if self.tampada:
            print("Erro: caneta tampada")
        elif self.cor:
            print(f"[bold {self.cor}]{texto}[/]")

canetaAzul = Caneta("Azul")
canetaAzul.destampar()
canetaAzul.escrever("oi")