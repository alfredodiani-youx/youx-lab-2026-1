distancia = float(input('Qual a distancia da sua viagem? '))
print('Voce esta prestes a comecar uma viagem de {}km.')
if  distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('E o preco da sua passagem sera de RS{:.2f}'.format(preco))

