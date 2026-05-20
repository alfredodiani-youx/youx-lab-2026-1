class Funcionario:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
    def Apresentacao(self):
            print(f'Olá, sou {self.nome} e sou {self.cargo} do setor {self.setor} da empresa.')

funcionario1 = Funcionario('Maria', 'Administrção', 'Diretora')
funcionario1.Apresentacao()
funcionario2 = Funcionario('Pedro', 'TI', 'Programador')
funcionario2.Apresentacao()