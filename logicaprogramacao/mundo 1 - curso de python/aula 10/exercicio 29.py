velocidade = float(input('Qual a velocidade do carro? '))
if velocidade > 80:
 print('Multado!')
 multa = (velocidade - 80) * 7
 print(f'Você deverá pagar uma multa de {multa}!')
else:
    print('Dirija com segurança, bom dia!')
