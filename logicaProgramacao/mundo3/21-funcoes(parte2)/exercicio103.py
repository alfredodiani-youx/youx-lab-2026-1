def ficha (n, g):
    if len(n) == 0:
        print(f'O jogador <desconhecido> fez {g} gol(s) no campeonato.')
    else:
        print(f'O jogador {n} fez {g} gol(s) no campeonato.')
n = str(input('Nome do jogador: '))
g = input('Número de gols: ')
if not g:
    g = 0
else:
    g = int(g)
ficha(n, g)