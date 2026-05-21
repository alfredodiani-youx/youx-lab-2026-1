velocidade = float(input('Qual e a velocidade atual do carro!' ))
if velocidade> 80:
    print('MULTADO! voce excedeu a velocidade maxima da pista que e 80km/h')
    multa = (velocidade-80) * 7
    print('voce deve pagar uma multa de {:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança! ')

