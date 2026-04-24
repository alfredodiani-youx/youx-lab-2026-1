n = int(input('Digite o primeiro numero de uma P.A.: '))
r = int(input('Digite a razão da P.A: '))
for p in range(1, 11):
    pa = n + (p - 1) * r
    print(pa)