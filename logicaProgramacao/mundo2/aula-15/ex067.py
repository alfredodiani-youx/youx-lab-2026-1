
while True:
    valor = int(input('Quer ver a tabuada de qual valor? '))
    if valor < 0:
        print('Tabuada encerrada.')
        break
    else:
        for contagem in range(0, 10):
            print(f'{valor} x {contagem+1} = {valor*(contagem+1)}')
