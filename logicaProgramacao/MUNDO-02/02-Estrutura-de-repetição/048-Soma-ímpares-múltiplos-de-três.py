somar = 0
conter = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        conter = conter + 1
        somar = somar + c
print('A soma de Todos os {} valores solicitados é {}'.format(conter, somar))

