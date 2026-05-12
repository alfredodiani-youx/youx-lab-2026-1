#Exercício Python 055: Faça um programa que leia o peso de cinco pessoas.
#No final, mostre qual foi o maior e o menor peso lidos.

maior_peso = 0
menor_peso = 0
for pessoa in range (1 , 6 ):
    peso = float(input("Digite seu peso(Kg): "))
    if peso == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < maior_peso:
            menor_peso = peso
print(f"O maior peso sera {maior_peso:.1f}Kg e o menor peso sera {menor_peso:.1f}Kg")

