from textwrap import shorten

times = ('América-MG', 'Athletico-PR', 'Atlético-MG', 'Bahia', 'Botafogo', 'Corinthians', 'Coritiba',
         'Cruzeiro', 'Cuiabá', 'Flamengo', 'Fluminense', 'Fortaleza', 'Goiás', 'Grêmio', 'Internacional', 'Palmeiras',
         'Bragantino', 'Santos', 'São Paulo', 'Vasco')
print(f'Os times são: {times}')
print('-=-=' * 20)
print()
print(f'Os primeiros 5 nomes são: {times[0:5]}')
print('-=-=' * 20)
print()
print(f'Os quato ultimos são: {times[-4:]}')
print('-=-=' * 20)
print()
print(f'Os times em ordem alfabetica: {sorted(times)}')
print('-=-=' * 20)