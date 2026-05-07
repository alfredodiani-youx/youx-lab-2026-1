numero = int(input('Quantos termos deseja mostrar? '))
a1 = 0
a2 = 1
print(f'{a1}->{a2}', end='')
cont = 3
while cont <= numero:
    a3 = a1 + a2
    print(f'-> {a3}', end='')
    cont += 1
    a1 = a2
    a2 = a3
print('FIM')