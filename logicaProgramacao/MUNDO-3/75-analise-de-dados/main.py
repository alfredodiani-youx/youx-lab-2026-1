lista = ''
pares = 0


for i in range(0,4):
    numero = int(input(f'digite o {i+1}° numero: '))
    if i == 0:
        primeiro = numero
    if numero % 2 == 0:
        pares += 1
    lista += f'{numero} '
    numeros = (lista.split())

print(f'voce digitou os valores {numeros}')
print(f'o numero {primeiro} apareceu {numeros.count(str(primeiro))} vezes')

if '3' in numeros:
    print(f'o numero 3 apareceu na {lista.split().index("3")+1}° posiçao')
else:
    print('o numero 3 nao apareceu em nenhuma posiçao')

print(f'ao todo foram digitados {pares} numeros pares')
