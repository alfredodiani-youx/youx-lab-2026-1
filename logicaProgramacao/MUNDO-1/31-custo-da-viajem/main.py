distancia = float(input('qual é a distancia da sua viajem? '))
print(f'voce esta para começar uma viajem de {distancia}km de distandia')
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print(f'o preco da sua passagem sera de R${preco}')