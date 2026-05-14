peso = float(input('Qual é seu peso?(Kg)'))
altura = float(input('Qual é sua altura?(m)'))
imc = peso / (altura ** 2)
print(f"O imc dessa pessoa é {(imc):.2f}")
if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc > 18.5 and imc < 25:
    print('Você está no peso ideal.')
elif imc > 25 and imc < 30:
    print('Você está sobrepeso.')
elif imc > 30 and imc < 40:
    print('Você está obeso.')
elif imc > 40:
    print('Você está com obesidade mórbida.')
