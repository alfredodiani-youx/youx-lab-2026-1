ab = int(input('Primeira reta: '))
bc = int(input('Segunda reta: '))
ac = int(input('Terceira reta: '))
if ab == bc == ac:
    print('Forma um triangulo equilatero')
elif ab == bc or bc == ac or ac == ab:
    print('Forma um triangulo isoceles')
elif (ab < bc + ac) and (ab < ac + bc) and (bc < ac + ac):
    print('Forma um triangulo escaleno')
else:
    print('Não forma um triangulo')