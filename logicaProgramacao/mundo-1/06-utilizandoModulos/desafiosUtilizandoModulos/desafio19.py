import random
n1 = input('Primeiro nome: ')
n2 = input('Segundo nome: ')
n3 = input('Terceiro nome: ')
n4 = input('Quarto nome: ')
s = random.choice([n1 , n2 ,n3 ,n4])
print('O escolhido foi {}' .format(s))