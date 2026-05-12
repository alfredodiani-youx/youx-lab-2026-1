tot = 0
N1 = (int(input('Digite um valor: ')),
      int(input('Digite outro valor: ')),
      int(input('Digite outro numero: ')),
      int(input('Digite o ultimo numero: ')))
print(f'Você digitou os valores: {N1}')
print(f'{f'O primeiro valor 3 apareceu na {N1.index(3)+1} posição.' if 3 in N1 else 'Não existem valores iguais a 3.'}')
tot2 = N1.count(9)
print(f'{'Não existem valores iguais a 9.' if tot2 <= 0 else (f'O valor 9 apareceu {tot2} {'vez' if tot2 == 1 else 'vezes'}.')}')
for n in N1:
    if n % 2 == 0:
        tot += 1
print(f'{'Não existem valores pares.' if tot <= 0 else 'O valor par digitado é: ' if tot == 1 else 'Os valores pares são: '}',end='')
for n in N1:
    if n % 2 == 0:
        print(n, end=' ')