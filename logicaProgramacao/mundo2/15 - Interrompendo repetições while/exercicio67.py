numero =  ''
while numero != -0:
    numero =int(input('digite um número  para mostrar sua tabuada:'))
    for t in range(1,11):
          print(f'{numero} x {t} = {numero * t}')