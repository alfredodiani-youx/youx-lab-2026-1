from random import randint
sorteio = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10) )
print('Os valores sorteados foram: ', end='')
for cont in sorteio:
    print(f'{cont} ', end='')
print(f'\nO maior valor sorteado foi {max(sorteio)}')
print(f'O menor valor sorteado foi {min(sorteio)}')