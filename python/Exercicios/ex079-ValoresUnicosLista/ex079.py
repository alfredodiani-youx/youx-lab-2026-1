lista = list()
while True:
    num = int(input('Digite um valor: '))
    if num not in lista:
        lista.append(num)
        print('Valor adicionado com sucesso!')
    else:
        print('Você já digtou esse valor! Isso não é permitido!')
    resposta = str(input('Deseja adicionar mais um? [S/N] '))
    if resposta in 'Nn':
        break
lista.sort()
print(f'Você digitou os números {lista}')