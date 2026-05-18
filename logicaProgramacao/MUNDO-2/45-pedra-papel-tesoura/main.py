from random import randint

materiais = ('pedra', 'papel', 'tesoura')

jogador1 = randint(0, 2)

print('''SUAS OPÇÕES SÃO:
[0] pedra
[1] papel
[2] tesoura''')

jogador2 = int(input('Qual é a jogada do jogador2? (0-2): '))

print(f'jogador1 escolheu {materiais[jogador1]}')
print(f'jogador2 escolheu {materiais[jogador2]}')

if jogador1 == 0:  # jogador1 jogou PEDRA

    if jogador2 == 0:

        print('EMPATE')

    elif jogador2 == 1:

        print('JOGADOR2 VENCEU!')

    elif jogador2 == 2:

        print('JOGADOR1 VENCEU!')

    else:

        print('JOGADA INVÁLIDA!')

elif jogador1 == 1:  # jogador1 jogou PAPEL

    if jogador2 == 0:

        print('JOGADOR1 VENCEU!')

    elif jogador2 == 1:

        print('EMPATE')

    elif jogador2 == 2:

        print('JOGADOR2 VENCEU!')

    else:

        print('JOGADA INVÁLIDA!')

elif jogador1 == 2:  # jogador1 jogou TESOURA

    if jogador2 == 0:

        print('JOGADOR2 VENCEU!')

    elif jogador2 == 1:

        print('JOGADOR1 VENCEU!')

    elif jogador2 == 2:

        print('EMPATE')

    else:

        print('JOGADA INVÁLIDA!')