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
        while self.comando in '@<>-+0':
            if self.ligado == False:
                print('TV desligada')
                self.comando = str(input('@ para ligar (0 encerrar programa) '))
                if self.comando not in '@<>-+0':
                    print('Comando inválido. Tente novamente.')
                    self.comando = str(input('@ para ligar (0 encerrar programa) '))
                if self.comando == '@':
                    self.ligado = True
                elif self.comando == '0':
                    break
            elif self.ligado == True:
                print('TV ligada.')
                self.comando = str(input(f'< CH{self.canal_atual} > - VOL{self.volume} + '))
                if self.comando not in '@<>-+':
                    print('Comando inválido. Tente novamente.')
                    self.comando = str(input(f'< CH{self.canal_atual} > - VOL{self.volume} + '))
                match self.comando:
                    case '<':
                        if self.canal_atual == self.canal_minino:
                            self.canal_atual = self.canal_maximo
                        else:
                            self.canal_atual -= 1
                    case '>':
                        if self.canal_atual == self.canal_maximo:
                            self.canal_atual = self.canal_minino
                        else:
                            self.canal_atual += 1
                    case '+':
                        if self.volume == self.volume_maximo:
                            self.volume = self.volume_maximo
                        else:
                            self.volume += 1
                    case '-':
                        if self.volume == self.volume_minimo:
                            self.volume = self.volume_minimo
                        else:
                            self.volume -= 1
                    case '@':
                        self.ligado = False


tv = ControleRemoto()
tv.controle()