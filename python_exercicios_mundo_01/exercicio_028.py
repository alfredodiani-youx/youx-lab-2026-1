from random import randint
from time import sleep
computador = randint (0 , 5)
print('Escolha um número entre 0 e 5')
print('Vou pensar em um número entre 0 e 5,tente adivinhe qual número pensei')
jogador = int(input('Em que número eu pensei?'))
if jogador== computador:
    print('Parabens vc ganhou o jogo')
    print('Eu pensei no número {} e você acertou afirmando que era o número {}'.format(computador, jogador))
else:
    print('Voce perdeu')
    print('Eu pensei no número {} e não no {}'.format(computador, jogador))
