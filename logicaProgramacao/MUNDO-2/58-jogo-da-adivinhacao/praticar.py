from random import randint
numero = randint(0,5)
chute = int(input('digite um valor: '))

tentativas = 1
while chute != numero:
    print("voce esta incorreto,digite novamente")
    chute = int(input('digite um valor: '))
    tentativas += 1
print(f'FIM,voce gastou {tentativas} tentativas')