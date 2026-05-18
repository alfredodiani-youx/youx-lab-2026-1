#Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

numero = int(input('digite um numero: '))
segundo = int(input('digite outro valor: '))
opcao = 0
while opcao != 5:
    print('[ 1 ] somar')
    print('[ 2 ] multiplicar')
    print('[ 3 ] maior')
    print('[ 4 ] novos números')
    print('[ 5 ] sair do programa')

    opcao = int(input('escolha uma opcao: '))
    if opcao == 1:
        print(f'a soma de {numero} + {segundo} = {numero+segundo}')
    if opcao == 2:
        print(f'a multiplicacao de {numero} x {segundo} = {numero*segundo}')
    if opcao == 3:
        if numero > segundo:
            print(f'{numero} é maior do que {segundo}')
        elif numero < segundo:
            print(f'{segundo} é maior do que {numero}')
    if opcao == 4:
        numero = int(input('digite outro numero: '))
        segundo = int(input('digite outro valor:  '))

