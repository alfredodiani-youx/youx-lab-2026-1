numero =int(input('digite um número:'))
total = 0
for  c in range(1,numero + 1):
   if  numero % c == 0:
       print('\033[33m', end=' ')
       total += 1
else:
    print('\033[31m', end= ' ')
    print(f'{c}')
print(f'\n\033[m O número  {numero} foi divisível {total} vezes')
if total == 2:
    print('Esse é um número primo.')
else:
    print('Esse não é um número primo.')