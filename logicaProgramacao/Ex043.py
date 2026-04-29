Peso = float(input('Qual o seu peso (Kg): '))
Altura = float(input('Qual sua altura (m): '))
Imc = Peso / (Altura**2)
print('O IMC dessa pessoa e de {:.1f}'.format(Imc))
if Imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= Imc < 25:
    print('Peso ideal')
elif 25 <= Imc < 30:
    print('Sobrepeso')
elif 30 <= Imc < 40:
    print('Obesidade')
elif Imc >= 40:
    print('Obesidade Morbida')