from random import randint
from time import sleep
from operator import itemgetter
print('Valores sorteados: ')
jogo = {}
for cont in range(1, 5):
    numero_atual = randint(1, 6)
    print(f'O jogador{cont} tirou {numero_atual}')
    jogo[f"jogador {cont}"] = numero_atual
    sleep(0.5)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for indice, valor in enumerate(ranking):
    print(f'{indice+1}º lugar: {valor[0]} com {valor[1]}')
print('-='*11)
print('Ranking dos jogadores:')
