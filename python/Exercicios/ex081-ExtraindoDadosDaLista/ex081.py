lista = list()
while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    resposta = str(input('Deseja adicionar mais um? [S/N] '))
    if resposta in 'Nn':
        break
print('-='* 17)
print(f'Você digitou {len(lista)} números.')
lista.sort(reverse= True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O número 5 está na lista!')
else:
    print('O número 5 não foi encontrado na lista')