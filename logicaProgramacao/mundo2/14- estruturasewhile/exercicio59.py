# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.


numero1 =int(input('digite seu primeiro valor:'))
numero2 =int(input('digite seu segundo valor:'))
opcao = 0
maior = 0
while  opcao !=5:
    print('[1] somar')
    print('[2] multiplicar')
    print('[3] maior')
    print('[4] novos números')
    print('[5] sair do programa')
    opcao =int(input('qual é sua opção?'))
    if opcao ==1:
        soma = numero1 + numero2
        print(f'a soma entre {numero1} e {numero2} é {soma}')
    elif opcao == 2:
        multiplicao = numero1 * numero2
        print(f'a multiplicação entre {numero1} x {numero2} é {multiplicao}')
    elif opcao == 3:
         if numero1 > numero2:
            maior = numero1
         else:
             maior = numero2
             print(f'entre {numero1} e {numero2} o valor  maior é  {maior}')
    elif opcao == 4:
        numero1 =int(input('digite outro valor:'))
        numero2= int(input('digite seu segundo valor:'))
    elif opcao == 5:
        print('finalizado....')
    else:
        print('opção invalida . tente novamente')
print('fim do progama. volte sempre')



