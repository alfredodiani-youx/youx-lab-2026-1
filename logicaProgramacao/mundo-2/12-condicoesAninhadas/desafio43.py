a = float(input('Qual e a sua altura? '))
p = float(input('Qual e o seu peso? '))
if p / a**2 < 18.5:
    print('Voce esta abaixo do peso')
elif p / a**2 > 18.5 and p / a**2 < 25:
    print('Voce esta no peso ideal')
elif p / a**2 > 25 and p / a**2 < 30:
    print('Voce esta com sobrepeso')
elif p / a**2 > 30 and p / a**2 < 40:
    print('Voce esta com obesidade')
else:
    print('Voce esta com obesidade mórbita')