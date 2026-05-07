peso =float(input('qual é seu peso? (kg)'))
altura =float(input('qual é sua altura? (m)'))
imc = peso  / (altura ** 2)
if imc > 40:
    print('OBESIDADE MÓRBIDA!')
elif imc > 30:
    print('OBESIDADE!')
elif imc > 25:
    print('SOBREPESO!')
elif imc > 18:
    print('PESO IDEAL!')
else:
    print('ABAIXO DO PESO!')

