numeros = [[], []]
for valor in range(0, 7):
    numero = (int(input(f'Digite o {valor+1}° valor: ')))
    numeros.append(numero)
    if numero % 2 == 0:
        numeros[0].append(numero)
    if numero % 2 != 0:
        numeros[1].append(numero)
numeros[0].sort()
print(f'Os valores pares digitados são {numeros[0]}')
numeros[1].sort()
print(f'Os valores ímapres digitados são {numeros[1]}')