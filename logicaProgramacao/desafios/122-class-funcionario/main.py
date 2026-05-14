class Funcionario:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentar(self):
        return f"Olá, prazer! meu nome é {self.nome} atualmente sou {self.cargo} no setor de {self.setor}"

funcionario = Funcionario(input("Nome: "), input("Setor: "), input("Cargo: "))
print(funcionario.apresentar())