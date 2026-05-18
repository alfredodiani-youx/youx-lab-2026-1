#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre
#todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer
#ou não continuar a digitar valores.

contagem = 0
continuar = 'S'
soma = 0
maior = menor = 0
while continuar in 'Ss':
    contagem += 1
    numero = int(input('digite um numero: '))
    if contagem == 1:
        maior = menor = numero
    elif numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero
    soma += numero
    continuar = input('quer continuar? [S/N]: ')

print(f'voce digitou {contagem} e a media foi {soma / contagem}')
print(f'o maior valor foi {maior} e o menor foi {menor}')




