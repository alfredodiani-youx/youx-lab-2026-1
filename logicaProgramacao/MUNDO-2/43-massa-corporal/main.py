peso = float(input('qual o seu peso?: '))
altura = float(input('qual a sua altura?: '))
imc = peso / altura ** 2
print(f' o imc é de {imc}')
if imc < 18.5:
    print('voce esta ABAIXO do peso')
elif imc >= 18.5 and imc <= 25:
    print('voce esta no PESO IDEAL')
elif imc > 25 and imc <=30:
    print('voce esta SOBREPESO')
elif imc > 30 and imc <=40:
    print('voce esta com OBESIDADE')
elif imc > 40:
    print('voce esta com OBESIDADE MORBIDA')