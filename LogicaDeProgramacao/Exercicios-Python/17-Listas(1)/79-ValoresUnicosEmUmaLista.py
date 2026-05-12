lista = []
N = int(input('Digite um valor: '))
print('Valor adicionado.')
lista.append(N)
SN = str(input('Quer continuar? [S/N] ').upper().strip())
while SN != 'N':
    N = int(input('Digite um valor: '))
    if N not in lista:
        lista.append(N)
        print('Valor adicionado.')
    else:
        print('Valor não adicionado.')
    SN = str(input('Quer continuar? [S/N] ').upper().strip())
lista.sort()
print('=-'*30)
print('Você adicionou os valores:', end=' ')
print(lista)