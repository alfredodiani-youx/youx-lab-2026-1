par = list()
impar = list()
while True:
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)
    resposta = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resposta in 'nN':
        break
print(f'Na lista par contém os números {par}')
print(f'Na lista ímpar contém os números {impar}')
print(f'A lista completa é {par + impar}')
