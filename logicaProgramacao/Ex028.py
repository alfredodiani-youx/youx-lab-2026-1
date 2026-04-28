from random import randint
numero = randint(0,5)
Tentativa = int(input('Tente adivinhar o numero entre 0 e 5: '))
print('PROCESSANDO...')
if Tentativa == numero:
    print('Parabens,eu pensei no numero {}'.format(numero))
else:
    print('Voce errou,tente novamente')