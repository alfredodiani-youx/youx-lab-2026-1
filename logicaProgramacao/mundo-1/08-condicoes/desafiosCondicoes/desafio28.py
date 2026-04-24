import random
n = random.randint(0,5)
r = int(input('Digite um numero de 0 a 5: '))
if r == n:
    print('Parabens! Voce acertou')
else:
    print('Voce errou')