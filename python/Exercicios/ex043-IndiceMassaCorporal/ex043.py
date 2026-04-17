peso = float(input('Qual seu peso atual (em Kg)? '))
altura = float(input('Qual sua altura (em metros)? '))
imc = peso / (altura ** 2)
print('Seu IMC é de {}'.format(imc))

if imc < 18.5:
    print('Você está abaixo do peso!')
elif 18.5 < imc <= 25:
    print('Você está no peso ideal!')
elif 25 < imc <= 30:
    print('Você está com sobrepeso!')
elif 30 < imc <= 40:
    print('Você está com obesidade!')
elif imc > 40:
    print('Você está com obesidade mórbida! Tome cuidado!')
