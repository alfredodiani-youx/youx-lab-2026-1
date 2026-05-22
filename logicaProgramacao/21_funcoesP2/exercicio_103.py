def ficha(nome, gols):
    if not nome:
        nome = '<desconhecido>'
    if not gols:
        gols = 0
    print(f'O jogador {nome} fez {gols} gols(s) no campeonato.')
nome = input('Nome do Jogador: ')
gols = input('Número de Gols: ')

ficha(nome, gols)