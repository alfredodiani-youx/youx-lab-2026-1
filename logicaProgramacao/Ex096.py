def area (larg,comp):
    a = larg * comp
    print(f'A area de um terreno {larg}x{comp} e {a}m')



print('CALCULADORA DE TERRENO')
l = float(input('Digite a largura: '))
c = float(input('Digite o comprimento: '))
area(l,c)