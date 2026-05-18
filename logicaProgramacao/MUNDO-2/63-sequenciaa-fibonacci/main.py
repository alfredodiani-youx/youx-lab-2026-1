#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
#Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8

numero = int(input('digite um numero e veja sua sequencia: '))
termo1 = 0
termo2 = 1
print(f'{termo1} - {termo2}',end='')
contagem = 3
while contagem <= numero:
    termo3 = termo1 + termo2
    print(f' - {termo3}',end='')
    termo1 = termo2
    termo2 = termo3
    contagem += 1
print(' FIM')
