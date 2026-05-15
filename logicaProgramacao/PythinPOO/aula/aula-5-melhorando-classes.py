class Gafanhoto:
    """
    Essa classe cria um gafanhoto, que é uma pesssoa que tem nome e idade.
    """
    def __init__(self, nome = '', idade = 0): # Metodo Construtor
        #Atributos
        self.nome = nome
        self.idade = idade

    #metodo de Instanvia
    def Aniversario(self):
        self.idade += 1

    # def Mensagem(self):
    #     return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade'

    # def __str__(self):
    #     return  'Vou te mostrar uma coisa...'

    def __str__(self):
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade'

    def __getstate__(self):
        return  f'Estado: nome = {self.nome} ; idade = {self.idade}'

#declaração de objetos
g1 = Gafanhoto('Maria', 17)
g1.Aniversario()
print(g1)
# print(g1.Mensagem())
print(g1.__dict__)# Attribute
print(g1.__getstate__()) # Method
print(g1.__class__)
print(g1.__doc__)
# g2 = Gafanhoto('Mauro', 54)
# print(g2)
# print(g2.__getstate__())

# print(g2.Mensagem())
#
# g3 = Gafanhoto('vazio')
# print(g3.Mensagem())

#print(g1.__doc__) #Dunder Attribute