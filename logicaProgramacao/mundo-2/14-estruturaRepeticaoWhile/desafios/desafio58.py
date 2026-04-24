import random
r = 0
pc = random.randint(0,10)
print('Adivinhe que numero estou pensando')
while pc != r:
    r = int(input('Digite um numero de 0 a 10: '))
print('Parabens você acertou')