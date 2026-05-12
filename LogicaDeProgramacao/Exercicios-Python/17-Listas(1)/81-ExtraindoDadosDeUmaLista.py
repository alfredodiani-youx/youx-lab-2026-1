lista = []
cont = 0
N = int(input('Digite um valor: '))
lista.append(N)
cont += 1
SN = str(input('Quer continuar? [S/N] ').upper().strip())
while SN != 'N':
    N = int(input('Digite um valor: '))
    lista.append(N)
    cont += 1
    SN = str(input('Quer continuar? [S/N] ').upper().strip())
if cont == 1:
    print(f'Você digitou {cont} elemento.')
else:
    print(f'Você digitou {cont} elementos.')
lista.sort(reverse=True)
if cont == 1:
    print(f'O valor digitado é: {lista}')
else:
    print(f'Os valores digitados em ordem decrescente são: {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não faz parte da lista.')