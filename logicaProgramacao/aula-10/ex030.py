from traceback import print_tb

numero = int(input('Me diga um numero qualquer' ))
resultado = numero % 2
if resultado == 0:
    print(f'O numero {numero} e PAR!')
else:
    print(f'O numero {numero} e IMPAR!')
