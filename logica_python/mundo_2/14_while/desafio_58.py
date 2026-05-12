import random
numeropc = random.randint(0, 10)
numero_usuario = int(input('qual numero voce vai escolher?'))
while numeropc != numero_usuario:
    if numero_usuario < numeropc:
        print('o numero e MAIOR')
        numero_usuario = int(input('qual numero voce vai escolher? '))

    else:
        print('o numero e MENOR')
        numero_usuario = int(input('qual numero voce vai escolher? '))
    print('voce acertou!')

