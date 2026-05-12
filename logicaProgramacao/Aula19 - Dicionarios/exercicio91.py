#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
#Guarde esses resultados em um dicionário em Python.
#No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter

jogada = { 'jogador1': randint(1, 6),
           'jogador2': randint(1, 6),
           'jogador3': randint(1, 6),
           'jogador4': randint(1, 6)}
ranking = list
for k, v in jogada.items():
    print(f"O {k} tirou {v}")
    sleep(0.6)
ranking = sorted(jogada.items(), key=itemgetter(1), reverse=True)
print(30 * '-')
print("RANKING DOS JOGADORES")
print(30 * '-')
for indice, valor in enumerate(ranking):
    print(f"{indice + 1} lugar: {valor[0]} com {valor[1]}")
    sleep(1)