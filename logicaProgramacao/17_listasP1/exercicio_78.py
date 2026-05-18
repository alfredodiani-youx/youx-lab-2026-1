#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final,
#mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

numeros = []
for cont in range(0, 5):
    numeros.append(int(input('digite um valor :')))
maior= max(numeros)
menor= min(numeros)
print(f'o maior numero é {maior}')
print(f'o menor numero é {menor}')

posicao = numeros.index(5)
print(f'o maior numero está na posicao {max(numeros)}')
print(f'o menor numero esta na {min(numeros)}')



