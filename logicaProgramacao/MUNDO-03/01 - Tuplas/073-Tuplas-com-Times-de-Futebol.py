times = ('Palmeiras' , 'Flamengo ' , 'Fluminense' , 'Sao Paulo' , 'Bahia' , 'Athletico' , 'Coritiba' , 'Bragantino' , 'Botafogo' , 'Vasco da gama' , 'EC Vitoria' , 'Atletico-MG' , 'Gremio' , 'Internacional' , 'Santos' , 'Cruzeiro' , 'Corinthians' , 'Mirassol' , 'Remo' , 'Chapecoense')

print(f"Os 5 primeiros sao os {times[0:5]}")
print(f"Os ultimos 4 times sao{times[15:]}")
print(f"Em ordem alfabetica fica {sorted(times)}")
print(f"O santos esta na {times.index("Santos")+1} posição ")