from random import randint
computador = randint(0, 5)
print('-*-' * 20)
print('Vou Pensar Em Um Numero Entre 0 e 5. Tente adivinhar...')
print('-*-' * 20)
jogador = int(input('o numero que eu pensei foi:' ))
if jogador == computador:
    print('PARABENS! voce conseguiu me vencer! ')
else:
    print('GANHEI! eu pensei no numero {} e nao no {}!'.format(computador, jogador))

