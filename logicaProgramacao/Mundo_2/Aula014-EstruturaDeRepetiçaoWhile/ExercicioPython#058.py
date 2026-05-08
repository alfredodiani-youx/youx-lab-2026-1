# Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random
numeropc = random.randint(0, 10)
numero_usuario = int(input('Qual numero voce vai escolher? '))
while numeropc != numero_usuario:
    if numero_usuario < numeropc:
        print('O numero é MAIOR')
        numero_usuario = int(input('Qual numero voce vai escolher? '))

    else:
        print('O numero é MENOR')
        numero_usuario = int(input('Qual numero voce vai escolher? '))
print('Voce ACERTOU!')
