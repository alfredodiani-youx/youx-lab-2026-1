dados = dict()
gols = list()
dados['nome'] = str(input('Nome: '))
jogos = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for cont in range(1, jogos+1):
    gols.append(int(input(f'Quantos gols na {cont}º partida? ')))
dados['gols'] = gols[:]
dados['total'] = sum(gols)
print('-='*20)
print(dados)
print('-='*20)
for key, valor in dados.items():
    print(f'O campo {key} tem valor de {valor}')
print('-='*20)
print(f'O jogador {dados["nome"]} jogou {jogos}')
for indice, valor in enumerate(dados['gols']):
    print(f'    => Na partida {indice}, fez {valor} gols.')
print(f'Foi um total de {dados["gols"]} gols')