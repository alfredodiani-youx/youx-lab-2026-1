import random

a = str(input('primeiro nome: '))
b = str(input('segundo nome: '))
c = str(input('terceiro nome: '))
d = str(input('quarto nome: '))
lista = [a,b,c,d]
n1 = random.shuffle (lista)
print ('A ordem de apresentação é {}'.format(lista))