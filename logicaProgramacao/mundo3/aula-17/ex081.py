lista = []
opcao = 's'
while opcao not in 'Nn':
    numeros = int(input('Digite seu numero: '))
    lista.append(numeros)
    opcao = input('Voce deseja continuar? [S/N] ')
    while opcao not in 'SsNn':
        print('OPÇAO INVALIDA')
        opcao = input('Voce deseja continuar? [S/N] ')

print(len(lista))
lista.sort(reverse=True)
print(lista)
if 5 in lista:
    print('O valor 5 foi digitado.')
