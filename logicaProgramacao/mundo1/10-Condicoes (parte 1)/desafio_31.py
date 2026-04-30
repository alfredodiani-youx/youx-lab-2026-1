distancia = float(input('Qual e a distancia da viagem?'))
print('Voce esta prestas a começar a viagem de {}Km.' .format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('E o preco da sua passagem sera de R${:.2F}' .format(preco))
