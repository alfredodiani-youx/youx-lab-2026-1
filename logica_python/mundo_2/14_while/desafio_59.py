operacao = 0
primeiro = int(input('primeiro valor: '))
segundo = int(input('segundo valor: '))
while operacao != 5:
    print('''
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    operacao = int(input('qual sua escolha: '))
    if operacao == 1:
        soma = primeiro + segundo
        print(f'a soma dos dois e: {primeiro} + {segundo} = {soma}')
    if operacao == 2 :
        multiplicar = primeiro * segundo
        print(f'a multiplicacao dos dois e: {primeiro} x {segundo} = {multiplicar}')
    if operacao == 3:
        if primeiro > segundo:
            print(f'o primeiro e maior')
        elif segundo > primeiro:
            print(f'O segundo  e maior')
    if operacao == 4:
        primeiro = int(input('primeiro valor: '))
        segundo = int(input('segundo valor: '))
