numeros = list()
numero = int(input('Digite um valor: '))
if numero not in numeros:
    numeros.append(numero)
    print('Valor adicionado com sucesso...')
else:
    print('Valor duplicado. Não vou adicionar...')
resposta = str(input('Quer continuar? [S/N] ')).upper()
while resposta == 'S':
    numero = int(input('Digite um valor: '))
    if numero not in numeros:
        numeros.append(numero)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado. Não vou adicionar...')
    resposta = str(input('Quer continuar? [S/N] ')).upper()
print('-='*30)
numeros.sort()
print(f'Você digitou os valores {numeros}')