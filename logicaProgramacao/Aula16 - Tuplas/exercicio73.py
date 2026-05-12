#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
#Depois mostre:

#a) Os 5 primeiros times.
#) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Chapecoense.
times = ('Palmeiras' , 'Flamengo ' , 'Fluminense' , 'Sao Paulo' , 'Bahia' , 'Athletico' , 'Coritiba' , 'Bragantino' , 'Botafogo' , 'Vasco da gama' , 'EC Vitoria' , 'Atletico-MG' , 'Gremio' , 'Internacional' , 'Santos' , 'Cruzeiro' , 'Corinthians' , 'Mirassol' , 'Remo' , 'Chapecoense')

print(f"Os 5 primeiros sao os {times[0:5]}")
print(f"Os ultimos 4 times sao{times[15:]}")
print(f"Em ordem alfabetica fica {sorted(times)}")
print(f"O Chapecoense esta na {times.index("Chapecoense")+1} posicao")
