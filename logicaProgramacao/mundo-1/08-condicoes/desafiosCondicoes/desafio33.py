n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))
n3 = int(input('Terceiro numero: '))

#menor numero
if n1 < n2 and n2 < n3:
    print(f'O numero {n1} e o menor')
if n1 > n2 and n2 > n3:
    print(f'O numero {n3} e o menor')
else:
    print(f'O numero {n2} e o menor')

#maior numero
if n1 < n2 and n2 < n3:
    print(f'O numero {n3} e o maior')
if n1 > n2 and n2 > n3:
    print(f'o numero {n1} e o maior')
else:
    print(f'O numero {n2} e o maior')