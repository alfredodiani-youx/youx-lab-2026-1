num = int(input('Digite Um Nùmero: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end='')
        tot += 1
    else:
        print('\033[32m', end='')
    print('{} '.format(c), end='')
print('o numero {} foi divisivel {} vezes'.format(num, tot))
if tot == 2:
    print('\033[32mE por isso que é PRIMO')
else:
    print('\033[33mE por isso que ele NÃO E PRIMO')