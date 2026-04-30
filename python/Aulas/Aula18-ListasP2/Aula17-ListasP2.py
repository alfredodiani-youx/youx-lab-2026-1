galera = list()
dado = list()
tmaior = tmenor = 0
for cont in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for pessoa in galera:
    if pessoa[1] >= 21:
        print(f'{pessoa[0]} é maior de idade')
        tmaior += 1
    else:
        print(f'{pessoa[0]} é maior de idade')
        tmenor += 1
print(f'Temos {tmaior} maiores e {tmenor} menores de idade.')
print(dado)
print(galera)
