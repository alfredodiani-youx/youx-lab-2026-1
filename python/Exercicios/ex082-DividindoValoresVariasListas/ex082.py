lista = list()
pares = list()
impares = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    resposta = str(input('Deseja adicionar mais um? [S/N] '))
    if resposta in 'Nn':
        break
for indice, valor in enumerate(lista):
    if valor % 2 == 0:
        pares.append(valor)
    elif valor % 2 == 1:
        impares.append(valor)
print(f'A lista completa é {lista}')
print(f'A lista de números pares é {pares}')
print(f'A lista de números ímpares é {impares}')