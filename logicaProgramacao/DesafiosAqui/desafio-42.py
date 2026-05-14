vl1=float(input('Primeiro segmento: '))
vl2=float(input('Segundo segmento: '))
vl3=float(input('Terceiro segmento: '))
if vl1 < vl2 + vl3 and vl2<vl1+vl3 and vl3<vl1+vl3:
    print ('Você pode fazer um triângulo')
    if vl1==vl2==vl3:
        print('EQUILÁTERO!')
    elif vl1==vl2:
        print('ISÓSCELES!')
    elif vl1==vl3:
        print('ISÓSCELES!')
    elif vl2==vl1:
        print('ISÓSCELES!')
    elif vl2==vl3:
        print('ISÓSCELES!')
    elif vl3==vl1:
        print('ISÓSCELES!')
    elif vl3==vl2:
        print('ISÓSCELES!')
    else:
        print('ESCALENO!')
else:
    print('Não é possível fazer um triangulo')
