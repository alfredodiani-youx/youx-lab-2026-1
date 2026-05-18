#faça um programa que calcule a soma entre todos os números impares que sao multiplos de tres
#e que se encontram no intervalo de 1 ate 500.


for n in range(1, 501):
    if n % 3 == 0:
        print(n, end=' ')
