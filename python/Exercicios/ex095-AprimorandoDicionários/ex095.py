time = list()
dados = dict()
gols = list()
resposta = ''
while resposta in 'Ss':
    dados.clear()
    dados['nome'] = str(input('Nome: '))
    jogos = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    gols.clear()
    for cont in range(1, jogos+1):
        gols.append(int(input(f'Quantos gols na {cont}º partida? ')))
    dados['gols'] = gols[:]
    dados['total'] = sum(gols)
    time.append(dados.copy())
    resposta = str(input('Deseja adicionar mais um? [S/N] '))
    if resposta not in 'SsNn':
        print('ERRO! Por favor, digite apenas S ou N.')
print('-='*30)
print('cod ', end='')
for elemento in dados.keys():
    print(f'{elemento:<15}', end='')
print()
print('-'*40)
for key, value in enumerate(time):
    print(f'{key:>3} ', end='')
    for dado in value.values():
        print(f'{str(dado):<15}', end='')
    print()
print('-'*40)
opcao = None
while opcao != 999:
    opcao = int(input('Mostrar dados de qual jogador? (999 para finalizar): '))
    if opcao >= len(time) and opcao != 999:
        print(f'ERRO! Não existe jogador com código {opcao}!')
    elif opcao == 999:
        break
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[opcao]["nome"]}:')
        for indice, quantgols in enumerate(time[opcao]['gols']):
            print(f'   No jogo {indice} fez {quantgols} gols')
print('<< VOLTE SEMPRE >>')