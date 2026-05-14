numero = 0
while numero >= 0:
    numero= int(input('Quer ver a tabuada de qual valor? '))
    tabuada = None
    tab = None
    for tabuada in range(1,11):
        tab = tabuada * numero
        if numero >0:
            print(f'{numero} X {tabuada} = {tab}')
        else:
            print('PROGRAMA DE TABUADA ENCERRADO. volte sempre!')
            break