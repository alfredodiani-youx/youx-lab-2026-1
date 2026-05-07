from random import randint
from time import sleep

numeros = []
def sorteia(a, b):
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(0, 5):
        numero = randint(a, b)
        numeros.append(numero)
        print(numero, end=' ')
        sleep(0.25)
    print('PRONTO!')

def somaPar(numeros):
    soma = 0
    for n in numeros:
        if n % 2 == 0:
            soma += n
    print(f'A soma dos valores pares de {numeros} é {soma}')

sorteia(1, 20)
somaPar(numeros)