from random import randint
from time import sleep
computador = randint(0, 5) # Faz o computador PENSAR!
print ('-=-' * 20)
print ('vou pensar em um numero de 0 a 5. tente adivinhar...')
print ('-=-' * 20)
jogador = int(input('Em que numero eu pensei?')) # Jogador tente adivinhar
print ('Processando...')
sleep(5)
if jogador == computador:
    print('PARABENS! Voce acertou!')
else:
    print(f'GANHEI! Eu pensei no numero {computador} e nao no numero {jogador}')
