continuar = 'S'
soma = quant = media= maior = menor = 0
while continuar == 'S':
    num = int(input('Digite um numero: '))
    print('-=-' * 10)
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    print('-=-' * 10)
    soma += num
    quant += 1

    if quant == 1:
        menor = maior = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    if continuar == 'N':
        media = soma / quant
        print(f'A media foi {media:.2f}')
        print(f"O menor numero foi {menor} e o maior {maior}")
        print('FIM DO PROGRAMA!')
