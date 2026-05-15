class Gafanhoto:
    def __init__(self):
        #Atributos
        self.nome = ''
        self.idade = 0

    #metodo de Instanvia
    def Aniversario(self):
        self.idade += 1

    def Mensagem(self):
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade'

#declaração de objetos
g1 = Gafanhoto()
g1.nome = "Maria"
g1.idade = 17
g1.Aniversario()
print(g1.Mensagem())

g2 = Gafanhoto()
g2.nome = 'Mauro'
g2.idade = 53
print(g2.Mensagem())