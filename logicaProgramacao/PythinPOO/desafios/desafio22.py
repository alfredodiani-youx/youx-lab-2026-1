class ControleRemoto:
    def __init__(self):
        self.canal_atual = 1
        self.canal_minino = 1
        self.canal_maximo = 5
        self.volume = 1
        self.volume_minimo = 0
        self.volume_maximo = 5
        self.ligado = False
        self.comando = ''
    def controle(self):
        self.comando = str(input('@ para ligar (0 encerrar programa) '))
        if self.comando not in '@<>-+0':
            print('Comando inválido. Tente novamente.')
            self.comando = str(input('@ para ligar (0 encerrar programa) '))
    def ligar(self):
        if self.comando == '@':
            self.ligado = True
    def desligar(self):
        self.ligado = False
        self.comando = str(input('@ para ligar (0 encerrar programa) '))
    def proximo_canal(self):
        if self.canal_atual == self.canal_maximo:
            self.canal_atual = self.canal_minino
        else:
            self.canal_atual += 1
    def canal_anterior(self):
        if self.canal_atual == self.canal_minino:
            self.canal_atual = self.canal_maximo
        else:
            self.canal_atual -= 1
    def aumentar_volume(self):
        if self.volume == self.volume_maximo:
            self.volume = self.volume_maximo
        else:
            self.volume += 1
    def diminuir_volume(self):
        if self.volume == self.volume_minimo:
            self.volume = self.volume_minimo
        else:
            self.volume -= 1
    def status(self):
        self.comando = str(input(f'< CH{self.canal_atual} > - VOL{self.volume} + '))
        if self.comando not in '@<>-+0':
            print('Comando inválido. Tente novamente.')
            self.comando = str(input(f'< CH{self.canal_atual} > - VOL{self.volume} + '))

tv = ControleRemoto()
tv.controle()
while tv.comando != '0':
    tv.status()
    match tv.comando:
        case '>':
            tv.proximo_canal()
        case '<':
            tv.canal_anterior()
        case '+':
            tv.aumentar_volume()
        case '_':
            tv.diminuir_volume()
        case '@':
            tv.desligar()