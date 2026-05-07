def área():
    area = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {area:.2f}m².')

largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
área()