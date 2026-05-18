#Faça um programa que leia um número qualquer e mostre o seu fatorial.

#Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

numero = int(input('DIGITE UM NUMERO: '))
fatorial = 1
calculo = numero
while calculo > 0:
    print(f'{calculo}',end='')
    if calculo > 1:
        print(' x ',end='')
    else:
        print(' = ',end='')
    fatorial *= calculo
    calculo -= 1
print(f'{fatorial}')