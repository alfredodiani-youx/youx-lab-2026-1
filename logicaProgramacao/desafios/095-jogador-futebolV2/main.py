jogadores = []
mostrar = 1
resposta = 'S'
while resposta == 'S':
    dados = {}
    gols_partida = []
    gols = 0
    dados['jogador'] = str(input('Nome: '))
    partidas = int(input('Quantas partidas ele(a) jogou? '))
    for i in range(0, partidas):
        gol = int(input(f"   Quantos gols {dados['jogador']} fez na partida {i + 1}°? "))
        gols_partida.append(gol)
        gols += gol
    dados['gols'] = gols_partida
    dados['total'] = gols
    jogadores.append(dados)
    resposta = str(input('Quer continuar? [S/N] ')).upper()
    while resposta not in 'NS':
        print('Resposta inválida. Tente novamente')
        continuar = str(input("Deseja  continuar? [S/N] ")).upper()
print('-='*30)
print(f'{'Cod.':<4}{'NOME':<20}{'GOLS'}{'TOTAL':>10}')
print('-'*40)
for c in range(0, len(jogadores)):
    print(f'{c:<4}{jogadores[c]['jogador']:<20}{jogadores[c]['gols']}{jogadores[c]['total']:>10}')
while mostrar != 999:
        print('-'*35)
        mostrar = int(input('Mostrar notas de qual jogador? (999 interrompe): '))
        if mostrar == 999:
            print('FINALIZANDO...')
        if mostrar <= len(jogadores) - 1:
            print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[mostrar]['jogador']}:')
            for i in range(0, len(jogadores[mostrar]['gols'])):
                print(f'   No jogo {i + 1} fez {jogadores[mostrar]['gols'][i]}.')