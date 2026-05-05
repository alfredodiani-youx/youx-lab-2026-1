reta1 = float(input('comprimento da primeira reta:'))
reta2 = float(input('comprimento da segunda reta:'))
reta3 = float(input('comprimento da terceira reta:'))
if reta1 == reta2  == reta3:
    print('equilatero')
elif reta1 == reta2:
    print('isoceles')
elif reta1 != reta2 != reta3:
    print('escaleno')
    print('os segmentos acima podem formar um triangulo')
elif  reta1 + reta2 > reta3 and reta1 + reta3 and reta2 + reta1:
    print(' os segmentos acima podem formar um triangulo')
else:
    print('os segmentos acima nao podem fromar um triangulo')
