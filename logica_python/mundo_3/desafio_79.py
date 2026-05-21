#Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
#Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

r ='s'
numeros = list()
while r == 's':
    n = int(input('digite um valor: '))
    if n not in numeros :
        numeros.append(n)
        print('valor adicionado com sucesso...')
else:
    print('valor duplicado! nao vou adicionar...')
    r= str(input('quer continuar?[s/n'))
    print('-=' * 30)
    numeros.sort()
    print(f'voce digitou os valores {numeros}')
