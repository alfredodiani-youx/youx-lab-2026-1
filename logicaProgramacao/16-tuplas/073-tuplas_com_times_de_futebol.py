times = ('corinthians', 'palmeiras', 'santos', 'gremio',
         'cruzeiro', 'flamengo', 'vasco', 'chapecoense'
         'atletico', 'botafogo', 'atletico-pr', 'bahia',
         'sao paulo', 'fluminense', 'sport recife',
         'ec vitoria', 'coritiba', 'avai', 'ponte preta',
         'atletico-go')
print('-='*15)
print(f'lista de times do brasileirao {times}')
print('-='*15)
print(f'os 5 primeiros sao {times[0:5]}')
print('-='*15)
print(f'os 4 ultimos sao {times[-4:]}')
print('-='*15)
print(f'times em ordem alfabetica: {sorted(times)}')
print('-='*15)
print(f'o chapecoense esta na {times.index(chapecoense)} posicao')
