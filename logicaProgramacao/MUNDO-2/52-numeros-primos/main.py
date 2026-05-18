#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

contador = 0
num = int(input('digite um numero: '))
for c in range (num, 0, 1):
    contador = contador + 1
if contador ==1:
    print(f'{num} É um numero primo')
else:
    print(f'{num} NAO é um numero primo')