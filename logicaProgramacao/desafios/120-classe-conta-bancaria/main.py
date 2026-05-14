class Conta:
    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.nome = nome
        self.saldo = saldo

    def __str__(self):
        return f"a conta id {self.id} pertence a {self.nome} e possui o saldo de R$ {self.saldo}"

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return f"Saque de R$ {valor:.2f} solicitado com sucesso!"
        else:
            return f"Saldo insuficiente para saque"
    def depositar(self, valor):
        self.saldo += valor
        return f"Deposito de R$ {valor:.2f} realizado com sucesso!"

c1 = Conta(1, "Joao", 90)
print(c1)
print(c1.sacar(90))
print(c1.depositar(90))