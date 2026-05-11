while True:
    Tabuada = float(input('Digite um numero pra ver sua tabuada: '))
    if Tabuada < 0:
        break
    print('-=-' * 10)
    for c in range(1, 11):
        print('{} x {} = {}'.format(Tabuada, c, Tabuada * c))
    print('-=-' * 10)
print('O PROGRAMA ACABOU! ')