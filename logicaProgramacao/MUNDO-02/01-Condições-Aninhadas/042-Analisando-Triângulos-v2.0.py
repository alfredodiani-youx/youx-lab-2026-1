r1 = float(input('Primeiro seguimento '))
r2 = float(input('Segundo seguimento  '))
r3 = float(input('Terceiro seguimento '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('os Seguimentos acima pode formar um triangulo ', end="")
if r1 == r2 == r3:
    print('EQUILÁTERO')
if r1 != r2 != r3:
    print('ESCALENO')
else:
    print('NAO E FORMA UM TRIANGOLO')