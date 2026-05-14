idade=int(input('Digite sua idade: '))
if idade<10:
    print('Categoria MIRIM')
elif idade<15:
    print('Categoria INFANTIL')
elif idade<20:
    print('JUNIOR')
elif idade <21:
    print('SÊNIOR')
else:
    print('MASTER')