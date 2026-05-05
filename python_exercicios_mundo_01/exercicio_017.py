from math import hypot
catetooposto = float(input('Comprimento do cateto oposto: '))
catetoadjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = hypot(catetooposto, catetoadjacente)
print('A hipotenusa vai medir {}'.format(hipotenusa))
