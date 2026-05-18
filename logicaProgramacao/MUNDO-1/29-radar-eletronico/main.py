velocidade = float(input('qual é a velocidade atual do carro?'))
if velocidade > 80:
    print('voce passou da velocidade permitida que é de 80km por hora')
    multa = (velocidade-80) * 7
    print(f'voce deve pagar uma multa no valor de R${multa}!')