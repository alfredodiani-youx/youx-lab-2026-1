d = 0
n = int(input('Digite um numero: '))
for c in range(1, n + 1):
    if n % c == 0:
        d += 1
if d == 2:
    print('O numero e primo')
else:
    print('O numero não e primo')