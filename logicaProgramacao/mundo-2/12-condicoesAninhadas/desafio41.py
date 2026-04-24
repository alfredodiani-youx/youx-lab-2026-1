print('Confederação Nacional de Natação')
idade = int(input('Qual a sua idade? '))
if idade <= 9:
    print('Voce eata na categoria Mirim')
elif idade > 9 and idade <= 14:
    print('Voce esta na categoria Infantil')
elif idade > 14 and idade <= 19:
    print('Voce esta na categoria Junior')
elif idade >19 and idade <=20:
    print('Voce esta na categoria Sênior')
else:
    print('Voce esta na categoria Master')