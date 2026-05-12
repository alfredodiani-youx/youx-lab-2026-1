#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
#A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint as ra
from time import sleep as sl
def sorteia(lista):
    print("")
    for cont in range(0, 5):
        n = ra(1,10)
        lista.append(n)
        print(f"{n}", end=' ')
        sl(0.5)
def sorteia_pares(listaPar):
    soma = 0
    for valor in listaPar:
        if valor % 2 == 0:
            soma += valor
    print(f"A soma dos pares é {soma}")
numeros = list()
sorteia(numeros)
sorteia_pares(numeros)
