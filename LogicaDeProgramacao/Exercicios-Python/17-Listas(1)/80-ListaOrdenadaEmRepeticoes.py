lista = []
M = int(input('Digite um valor: '))
print('Numero adicionado ao final da lista.')
lista.append(M)
numMin = M
numMax = M
timer1 = 0
numMad = M
for i in range(4):
    N = int(input('Digite um valor: '))
    if N > numMax:
        print('Numero adicionado ao final da lista.')
        numMax = N
        lista.append(N)
    elif N < numMin:
        print('Numero adicionado a posição 0 da lista.')
        numMin = N
        lista.append(N)
    elif N > numMin and N < numMax:
        if timer1 == 0 or N < numMad:
            print('Numero adicionado a posição 1 da lista.')
            numMad = N
            lista.append(N)
            timer1 += 1
        elif timer1 == 1:
            print('Numero adicionado a posição 2 da lista.')
            numMad = N
            lista.append(N)
            timer1 += 1
        elif timer1 == 2:
            print('Numero adicionado a posição 3 da lista.')
            numMad = N
            lista.append(N)
            timer1 += 1
lista.sort()
print(f'Os valores digitados são: {lista}')