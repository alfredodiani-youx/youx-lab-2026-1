temp = []
principal = []
resposta = 'S'
maior = menor = 0
while resposta == 'S':
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(principal) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    principal.append(temp[:])
    temp.clear()
    resposta = str(input('Quer continuar? [S/N] ')).upper()
    while resposta not in 'NS':
        print('Resposta inválida.Tente novamente.')
        resposta = str(input('Quer continuar? [S/N] ')).upper()
print('-'*30)
print(f'Ao todo, você cadastrou {len(principal)} pessoas')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for pessoa in principal:
    if pessoa[1] == maior:
        print(f'[{pessoa[0]}] ', end='')
print(f'\nO menor peso foi de {menor}Kg. Peso de ', end='')
for pessoa in principal:
    if pessoa[1] == menor:
        print(f'[{pessoa[0]}] ', end='')