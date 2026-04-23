import math

O = float(input('Digite o valor do cateto oposto: '))
A = float(input('Digite o valor do cateto adjacente: '))
hi = math.hypot(O, A)
print('A hipotenusa  vai medir {:.2f}'.format(hi))
