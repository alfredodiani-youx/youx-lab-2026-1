distancia = float(input('Qual é a distancia da viagem? '))
print('Sua viagem é de {}'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
    print('O preco total a pagar é {}'.format(preco))
