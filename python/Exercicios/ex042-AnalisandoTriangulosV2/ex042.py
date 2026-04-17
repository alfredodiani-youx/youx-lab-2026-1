a = float(input('Digite o valor da primeira reta: '))
b= float(input('Digite o valor da segunda reta: '))
c = float(input('Digite o valor da terceira reta: '))

if (a < b + c) and (b < a + c) and (c < a + b):
    print('Essas retas podem formar um triângulo!')
    if (a == b == c):
        print('Será formado um triângulo Equilátero!')
    elif (a == b != c) or (b == a != c) or (c == b != a):
        print('Será formado um triângulo Isóceles')
    elif (a != b != c):
        print('Será formado um triângulo Escaleno')
else:
    print('As restas não podem formar um triângulo!')

