class Lutador: # declaração classe
    """
    essa class crie um objeto lutador e logo após retorna dados registrados
    """
    def __init__(self, n, i, p): #Método construtor
        #atributos instancias:
        self.nome = n
        self.idade = i
        self.peso = p
        self.wins = 0

    def lutar(self):
        self.wins += 1
    def mensagem(self):
        return f"{self.nome} tem {self.idade} anos e {self.peso}kg, seu cartel tem {self.wins} vitorias"
    def __str__(self):
        return lutador.mensagem()

#nome = input("Digite o nome do lutador: ")
#idade = int(input("Digite a idade: "))
#peso = float(input("Digite o peso: "))
lutador = Lutador("joao", 17, 69)
lutador.lutar()
print(lutador.mensagem())
print(lutador.__doc__)
print(lutador)
print(lutador.__dict__)