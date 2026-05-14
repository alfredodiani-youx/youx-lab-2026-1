#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso,
#mostre a listagem de números gerados e tambem indique o menor e o maior valor que estao na tupla.

from random import randint
numero= randint (0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)
print(f'eu escolhi o valor {numero}')
for n in numero:
    print(f'{n}',  end=' ')
print(f'o maior numero é o {max(numero)}')
print(f'o menor numero foi o {min(numero)}')