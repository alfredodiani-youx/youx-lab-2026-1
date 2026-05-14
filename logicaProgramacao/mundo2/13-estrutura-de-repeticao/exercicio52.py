#Exercício Python 052: Faça um programa que leia um número inteiro
# e diga se ele é ou não um número primo.
numero =int(input('digite um número:'))
total = 0
for c in range(1,numero + 1):
   if  numero % c == 0:
       print('\033[33m', end=' ')
       total += 1
else:
    print('\033[31m', end= ' ')
    print(f'{c}')
print(f'\n\033[m o numero  {numero} foi divisivil {total} vezes')
if total == 2:
    print('por isso ele é um numero primo')
else:
    print('e por ele não é primo')

