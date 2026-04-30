from random import  randint
from time import sleep

list = []
print('-'*30)
print('     JOGO DA MEGA SENA     ')
print('-'*30)
numero = int(input('Quantos jogos você quer sortear? '))
print('-='*5,f"SORTEANDO {numero} JOGOS", '-='*5)
for i in range(0, numero):
    jogos = []
    while len(jogos) != 6:
        aleatorio = randint(1, 60)
        if aleatorio not in jogos:
            jogos.append(aleatorio)
        jogos.sort()
    list.append(jogos[:])
    print(f'O jogo {i+1}:{jogos}')
    sleep(1)
print("-=" * 5, '< BOA SORTE! >', "-=" * 5)