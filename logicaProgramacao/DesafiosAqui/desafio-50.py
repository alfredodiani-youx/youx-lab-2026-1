print('digite um números em cada um dos 6:')
n1=int(input('R: '))
n2=int(input('R: '))
n3=int(input('R: '))
n4=int(input('R: '))
n5=int(input('R: '))
n6=int(input('R: '))
soma=None
if (n1+n3+n4+n5+n6+n2)%2==0:
    soma=(n1+n2+n3+n4+n5+n6)
    print (f'A soma entre eles deu: {soma}')
else:
    print('erro.')

