
#Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
#do Campeonato Brasileiro de Futebol,
#na ordem de colocação. Depois mostre:

times = ('corinthians', 'palmeras', 'santos',
'gremio', 'cruzeiro o maior de todos','flamengo', 'vasco', 'chapecoense',
'atletico menor de todos', 'bota fogo', 'atletico paranaence PR', 'sao paulo', 'fluminense', 'sport recife', 'ec vitori',
'curitiba', 'avai', 'ponte preta', 'atletico-go')

print('-=' * 15)
print(f'Lista de times do Brasileirao: {times}')
print('-=' * 15)
print(f'Os 5 primeiros sao times {times[0:5]}')
print('-=' * 15)
print(f'Os ultimos sao {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabetica: {sorted(times)}')
print('-=' * 15)
print(f'O chapecoense esta na {times.index("chapecoense")} posiçao')
