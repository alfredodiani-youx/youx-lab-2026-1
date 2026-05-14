times= ('palmeiras', 'flamengo', 'fluminense', 'sao paulo', 'athletico paranaense',
        'bahia', 'red bull bragantino                                                                          '
         'vasco', 'coritiba', 'vitoria', 'cruzeiro', 'botafogo',
         'atletico mineiro', 'internacional', 'santos',
         'corinthias' 'gremio', 'mirassol', 'remo', 'chapecoense')

print(f'lista dos times do brasileirao{times}')
print(f'os primeiros times sao {times[0:5]}')
print(f'os 4 ultimos times sao {times[-4:]}')
print(f'os times em ordem alfabetica ficaria {sorted(times)}')
print(f'o chapecoense está na {times.index('chapecoense')} posição')