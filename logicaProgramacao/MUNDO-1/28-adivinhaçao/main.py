from random import randint
r = randint(0,5)
print('-='*25)
print('vou pensar em um numero entre 0 e 5.tente adivinhar')

nd = int(input('digite um numero entre 0 e 5: '))
if nd == r:
    print('voce ganhou')
else:
    print('voce perdeu')