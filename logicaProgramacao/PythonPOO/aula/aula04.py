#Declaração de Classe

class Gafanhoto:
    '''
    Essa classe cria um Gafanhoto, que é uma pessoa que tem nome e idade.

    Para criar uma nova pessoa, use:
    variável = Gafanhoto(nome, idade)
    '''
    def __init__(self, nome='vazio', idade=0): #Método Construtor
        #Atributos de Instância
        self.nome = nome
        self.idade = idade

        #Métodos de Instância
    def aniversário(self):
        self.idade = self.idade + 1

    def mensagem(self):
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade.'

    def __str__(self):
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade.'

    def __getstate__(self):
        return f'Estado: nome = {self.nome}; idade = {self.idade}'

g1 = Gafanhoto('Maria', 17)
g1.aniversário()
print(g1.__doc__) #___doc___ é o help
print(g1)
print(g1.__dict__)
print(g1.__getstate__())
print(g1.__class__)

g2 = Gafanhoto('Mauro', 23)
g2.aniversário()
print(g2)
print(g2.__getstate__())
print(g2.__class__)

g3 = Gafanhoto()
print(g3)