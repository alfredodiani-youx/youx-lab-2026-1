distancia = float(input('qual e a distancia de sua viagem?'))
print('voce esta preste a fazer uma viagem de {}km.'.format(distancia ))
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('o preço de sua passagem será de R${:.2f}'.format(preco))