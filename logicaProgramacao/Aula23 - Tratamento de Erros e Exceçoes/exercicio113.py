#Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido.
#Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaint(msg):
    while True:
        try:
            numero = int(input(msg))
        except (ValueError, TypeError):
            print("ERRO: por favor, digite um numero inteiro valido. ")
            continue
        else:
            return numero
num = leiaint("Digite um valor: ")
print(f"O valor digitado foi {num}")
