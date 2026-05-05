from datetime import date
atual = date.today().year
nascimento = int(input('qual a data de nascimento do atleta?'))
idade= atual - nascimento
print(f'o atleta tem {idade}')
if idade <= 9:
    print('voce é mirin')
elif idade <= 14:
    print(' voce é ifantil')
elif idade <=19:
    print(' voce é junior ')
elif idade <=25:
    print('voce é senior')
else:
    print('voce é master')