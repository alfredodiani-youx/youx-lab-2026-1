from random import randint
print('Escolha uma das opcoes para jogar:')
print('[ 1 ] PEDRA')
print('[ 2 ] PAPEL')
print('[ 3 ] TESOURA')
opcao = int(input('Sua opcao: '))
OpcaoDoComputador = ['PEDRA', 'PAPEL', 'TESOURA']
OpcaoDoComputador2 = randint(1, 3)
print(f'O Jogador escolheu {opcao} e o Computador escolheu {OpcaoDoComputador2}')
if opcao == OpcaoDoComputador2:
    print('Empate')
elif opcao == 2 and OpcaoDoComputador2 == 3 or opcao == 1 and OpcaoDoComputador2 == 2 or opcao == 3 and OpcaoDoComputador2 == 2:
    print('VOCE PERDEU')
elif opcao == 2 and OpcaoDoComputador2 == 1  or opcao == 3 and OpcaoDoComputador2 == 2 or opcao == 1 and OpcaoDoComputador2 == 3:
    print('VOCE GANHOU')