Numero = int(input('Digite um numero inteiro: '))
tot = 0
for c in range(1, Numero +1):
    if Numero % c == 0:
        tot += 1
print(f'O numero {Numero} foi dividido {tot} vezes')
if tot == 2:
    print(f'O numero {Numero} foi primo')
else:
    print(f'O numero {Numero} nao foi primo')