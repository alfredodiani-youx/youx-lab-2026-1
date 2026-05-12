listaNum = []
listaMax = []
listaMin = []
timer1 = 0
numMax = 0
numMin = 0
for c in range(5):
    n = int(input(f'Digite um numero da posição {c}:'))
    listaNum.append(n)
    if timer1 == 0:
        numMin = n
        numMax = n
        timer1 += 1
    if timer1 >= 1:
        if numMax < n:
            numMax = n
        elif numMin > n:
            numMin = n
for d in listaNum:
    if d == numMax:
        listaMax.append(d)
    else:
        listaMax.append(0)
    if d == numMin:
        listaMin.append(d)
    else:
        listaMin.append(0)
print(f'Você digitou os valores: {listaNum}')
print(f'O maior valor digitado é {numMax} e esta nas posições:', end=' ')
for i, v in enumerate(listaMax):
    if v == numMax:
        print(i,end='.. ')
print()
print(f'O menor valor digitado é {numMin} e esta nas posições:', end=' ')
for i, v in enumerate(listaMin):
    if v == numMin:
        print(i,end='.. ')

