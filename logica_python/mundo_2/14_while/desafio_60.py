numero = int(input('Digite um numero para ver seu fatorial:  '))
contador = numero
print(f'Calculando {numero}! = ', end='')
fatorial = 1
while contador > 0:
    print(f'{contador}', end='')
    print(f' x ' if contador > 1 else " = ", end='')
    fatorial *= contador
    contador -= 1
print(f'{fatorial}.')
