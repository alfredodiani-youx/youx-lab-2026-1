from random import randint
def sortear(lista):
    for c in range(5):
        numero= randint(1, 10)
        lista.append(numero)
    print(f'sorteando valores da lista {lista}')
def soma(lista):
    s= sum(lista)
    print(f'somando os valores de {lista} teremos {s}')
numeros= []
sortear(numeros)
soma(numeros)