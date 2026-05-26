valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    cont = str(input('Quer continuar? [S/N] '))
    while cont not in 'SsNn':
        cont = str(input('Resposta não válida! Quer continuar? [S/N] '))
    if cont in 'Nn':
        break
valores.sort(reverse=True)
print(f'Você digitou {len(valores)} elementos!')
print(f'Os valores em ordem decrescente são {valores}')
if 5 not in valores:
    print('O valor 5 não faz parte da lista!')
else:
    print('O valor 5 faz parte da lista!')