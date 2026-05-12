#Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
#Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8

n = int(input('Digite um numero: '))
contador = 0
atual = 0
ultimo = 0
while contador < n:
    if contador == 0:
        print(atual)
        contador += 1
    elif contador == 1:
        atual = 1
        print(atual)
        contador += 1
    else:
        resultado = atual + ultimo
        print(resultado)
        ultimo = atual
        atual = resultado
        contador += 1



