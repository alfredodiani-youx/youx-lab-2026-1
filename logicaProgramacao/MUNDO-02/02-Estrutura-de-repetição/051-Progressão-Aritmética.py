print('\033[33m====' * 16)
print('                     10 TERMOS DE UMA P.A')
print('====' * 16)
T = int(input('Primeiro Termo: '))
R = int(input('Razão: '))
D = T + (10 - 1) * R
for c in range(T, D + R + R, R  ):
    print('{} '.format(c), end= ' ➜ ' )
#FIM
print('ACABOU!!!')
print('\033[33m====' * 16)