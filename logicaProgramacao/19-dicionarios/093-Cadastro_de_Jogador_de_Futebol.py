dados = {}
dados['nome'] = input('Nome: ')
dados['partidas'] = int(input('Quantidade de partidas: '))
gols = list()
for i in range(dados['partidas']):
    print(f'Quantos gols na partida {i+1}? ')
    n_gols = int(input())
    gols.append(n_gols)
    dados['gols'] = gols
    dados['total'] = sum(gols)
print('=-' * 90)
print(dados)
print('=-' * 90)
for k,v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('=-' * 90)
print(f'O/A jogador/a {dados["nome"]} jogou {dados["partidas"]} partidas')
for k, v in enumerate(gols):
    print(f'Na partida {k+1}, fez {v}')
print(f'Foi um total de {dados["total"]} gols')