while True:
    numero = int(input('Digite o número para a tabuada: '))
    if numero > 0:
        for tabuada in range(1, 11):
            print(f'{numero} * {numero * tabuada:2} = {numero * tabuada}')
    else:
        print('Programa de tabuada encerrado!')