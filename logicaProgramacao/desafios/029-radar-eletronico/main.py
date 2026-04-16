v = int(input('Qual é a velocidade atual do carro? '));
if v >= 80:
    print('MULTADO! Você excedeu o limite permitido que é 80KM/h\nVocê deve pagar uma multa de R${}'.format((v -79) * 7));
print('Tenha um bom dia! Dirija com segurança!');