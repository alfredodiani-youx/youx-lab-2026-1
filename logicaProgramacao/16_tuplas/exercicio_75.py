#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.

numeros = (int(input('digite um numero: ')),  int(input('digite um numero: ')),  int(input('digite um numero: ')), int(input('digite um numero: ')))
print(f'o numero nove apareceu {numeros.count (9)} vezes')
for i in numeros:
    print(f'o numero 3 aparece na {numeros.index (3)+1} posição')
    print('os valores pares digitados foram', end= ' ')
    for n in numeros:
        if n % 2 == 0:
             print(n, end= ' ')





