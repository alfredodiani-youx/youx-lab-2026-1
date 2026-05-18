#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo

frase = input('digite uma frase: ')
if frase == frase[:: -1]:
    print('é um polindromo')
else:
    print('nao é um polindromo')
