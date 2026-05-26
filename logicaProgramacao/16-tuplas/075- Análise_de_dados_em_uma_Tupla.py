numero =(int(input('digite um numero: ')),
        int(input('digite outro numero: ')),
        int(input('digite mais um numero: ')),
        int(input('digite o ultimo numero: ')))
print(f'voce digitou os valores {numero}')
print(f'o valor 9 apareceu {numero.count(9)} vezes')
if 3 in numero:
    print(f'o valor 3 apareceu na {numero.index(3)+1} posicao')
else:
    print('o valor 3 nao foi digitado em nenhuma posicao')
print('os valores pares digitados foram ', end='')
for n in numero:
    if n % 2 == 0:
        print(n, end=' ')



