linha1 = []
linha2 = []
linha3 = []
for lado in range(3):
    for c in range(3):
        valor =int(input(f'um valor para {lado, c}: '))
        if lado == 0:
            linha1.append(valor)
        elif lado == 1:
            linha2.append(valor)
        elif lado == 2:
            linha3.append(valor)
for lado in linha1:
    print([lado], end=" ")
print()
for lado in linha2:
    print([lado], end=" ")
print()
for lado in linha3:
    print([lado], end=" ")






