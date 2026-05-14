class Lutador: # declaração classe
    def __init__(self): #Método construtor
        #atributos instancias:
        self.nome = ""
        self.idade = 0
        self.peso = ""
        self.wins = 0

    def lutar(self):
        self.wins += 1
    def mensagem(self):
        return f"{self.nome} tem {self.idade} anos e {self.peso}kg, seu cartel tem {self.wins} vitorias"

lutador = Lutador()
lutador.nome = input("Digite o nome do lutador: ")
lutador.idade = int(input("Digite a idade: "))
lutador.peso = float(input("Digite o peso: "))
lutador.lutar()
print(lutador.mensagem())