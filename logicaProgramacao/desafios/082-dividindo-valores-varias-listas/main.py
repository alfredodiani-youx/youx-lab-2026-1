numeros = list()
par = list()
impar = list()
resposta = "S"
while resposta == 'S':
    numero = int(input('Digite um valor: '))
    numeros.append(numero)
    if numero % 2 == 0:
        par.append(numero)
    if numero % 2 != 0:
        impar.append(numero)
    resposta = str(input('Quer continuar? [S/N] ')).upper()
    while resposta not in 'NS':
        print('Resposta inválida. Tente novamente!')
        resposta = str(input('Quer continuar? [S/N] ')).upper()
print('-=' * 30)
print(f'A lista completa é {numeros}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')