numeros = [[]], [[]]
valor = 0
for cont in range(1, 8):
    numeros =int(input(f'digite o {cont}° numero: '))
if numeros % 2 == 0:
    numeros[0].append(valor)
else:
    numeros[1].append(valor)