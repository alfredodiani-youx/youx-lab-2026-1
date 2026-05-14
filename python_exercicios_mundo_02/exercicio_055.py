#Exercício Python 055: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior
# e o menor peso lidos.

maior = 0
menor = 0
contador = 0
for pessoa in range(1,6):
    peso = float(input(f"Qual é o peso da {pessoa} pessoa: "))
    contador += 1
    if contador == 1:
        maior = peso
        menor = peso
    if maior > peso:
        maior == peso
    elif menor < peso:
        menor == peso
print(f"O maior peso lido foi de {maior}")
print(f"O menor peso lido foi de {menor}")
