velocidade = float(input('Qual é a sua velocidade atuamente? '))
if velocidade > 80:
    print('Vc passou do limite permitido que é 80km')
    multa = (velocidade - 80) * 7
    print('Vc vai pagar a multa de {} reais'.format(multa))
print('Tenha um bom dia e dirija com segurança')
