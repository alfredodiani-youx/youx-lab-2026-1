
numeros = []
pares = []
impares = []

while True:
    contagem = int(input('digite um numero: '))
    numeros.append(contagem)

    if contagem % 2 == 0:
        pares.append(contagem)

    else:
        impares.append(contagem)

    opcao = input('quer continuar [S/N]')

    if opcao in 'Nn':
        break

print("=>"*30)

print(f'a lista COMPLETA é {numeros}')
print(f'lista dos numeros PARES digitados é {pares}')
print(f'a lista dos numero IMPARES é {impares}')