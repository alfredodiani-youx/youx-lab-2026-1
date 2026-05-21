# exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120


numero =int(input('digite um número para calcular seu fatorial:'))
conta = numero
fatorial = 1
print(f'calculando {numero}! = ',end= "")
while conta > 0:
    print(f'{conta}', end= ' ')
    print('x' if conta > 1 else '=' ,end=' ')
    fatorial *= conta
    conta -= 1
print(f'{fatorial}')
