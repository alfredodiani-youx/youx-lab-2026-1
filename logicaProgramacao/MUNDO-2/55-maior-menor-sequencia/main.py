# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

ma = 0
me = 0
for n in range(5):
    peso = float(input(f'digite o peso da {n+1}° pessoa: '))
    if n == 0:
        ma = peso
        me = peso
    else:
        if peso >= ma:
           ma = peso
        if peso <= me:
           me = peso
print(f'dados os 5 pesos analisados o maior foi {ma} e o menor foi {me}')
