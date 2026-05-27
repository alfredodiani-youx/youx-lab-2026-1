time = list()
jogador = dict()
partidas = list()
pare = 0
resp = None
while True:
    jogador['nome'] = str(input('Nome do jogador:  '))
    tot = int(input(f'Quantas partidas o jogador {jogador['nome']} jogou? '))
    for c in range(0, tot):
        partidas.append(int(input(f'   Quantos gols na partida {c+1}: ')))
    jogador['gols'] = partidas[:]
    jogador['toral'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resposta = str(input('Quer continuar? [S/N] '))
        resp = resposta.upper().strip()
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp =='N':
        break
print('≃~'*30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}',end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>3} ',end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)
while True:
    busca = int(input('Mostrar dados de qual jogador? '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com esse código')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]['nome']}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   No jogo {i} fez {g} gols')
    print('-'*40)
print('<< VOLTE SEMPRE >>')