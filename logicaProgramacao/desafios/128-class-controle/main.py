from rich import print
from rich.emoji import Emoji
from rich.panel import Panel

class Controle:
    def __init__(self):
        self.ligada = False
        self.canal = 1
        self.volume = 1

    def controle(self, comando):
        if self.ligada:
            if comando == "@":
                self.ligada = False
            elif comando == "<":
                if self.canal != 1:
                    self.canal -= 1
                print(self.status())
                self.controle(input(f"< CH{self.canal} >   - VOL{self.volume} + "))
            elif comando == ">":
                if self.canal != 4:
                    self.canal += 1
                print(self.status())
                self.controle(input(f"< CH{self.canal} >   - VOL{self.volume} + "))
            elif comando == "-":
                if self.volume != 4:
                    self.volume -= 1
                print(self.status())
                self.controle(input(f"< CH{self.canal} >   - VOL{self.volume} + "))
            elif comando == "+":
                if self.volume != 4:
                    self.volume += 1
                print(self.status())
                self.controle(input(f"< CH{self.canal} >   - VOL{self.volume} + "))
        elif not self.ligada:
            print(self.status())
            print(f":level_slider: - Use @ para ligar-la: ", end="")
            if input().strip() == "@":
                self.ligada = True
                self.controle(comando)


    def status(self):
        if not self.ligada:
            print("\n\n\n\n\n\n\n")
            aviso = Panel(":prohibited: A Tv está desligada!", title="[ TV ]", width=30)
            return aviso
        elif self.ligada:
            print("\n\n\n\n\n\n\n")
            canais = [1,2,3,4]
            volume = [1,2,3,4]
            canalAtual = ""
            volumeAtual = ""
            for i in canais:
                if i == self.canal:
                    canalAtual += f"[bold on yellow] {i} [/]"
                else:
                    canalAtual += f" {i} "
            for i in volume:
                if i == self.volume:
                    volumeAtual += f"[on blue]  [/]"
                else:
                    volumeAtual += f"[on white]  [/]"
            aviso = Panel(f"CANAL = {canalAtual}\n\nVOLUME = {volumeAtual}", title="[ TV ]", width=40)
            return aviso


c1 = Controle()
c1.controle("<")