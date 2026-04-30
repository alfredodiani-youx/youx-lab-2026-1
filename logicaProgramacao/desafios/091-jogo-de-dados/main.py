from operator import itemgetter
from random import randint
from time import sleep

numeros = {'Jogador1': randint(1, 10), 'Jogador2': randint(0,10), 'Jogador3': randint(1, 10),
           'Jogador4': randint(1, 10)}
ranking = list()
print('>>>>> VALORES SORTEADOS <<<<<')
for k, v in numeros.items():
    print(f'{k} tirou {v}')
    sleep(0.5)
ranking = sorted(numeros.items(), key=itemgetter(1), reverse=True)
print('>>>>> RANKING DOS JOGADORES <<<<<')
for i, v in enumerate(ranking):
    print(f'  {i+1}° lugar: {v[0]} com {v[1]}.')
    sleep(0.5)
