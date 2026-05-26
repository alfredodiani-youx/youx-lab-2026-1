from random import randint
numeros = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print('os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\no maior valor digitado foi',max(numeros))
print(f'o menor valor digitado foi',min(numeros))