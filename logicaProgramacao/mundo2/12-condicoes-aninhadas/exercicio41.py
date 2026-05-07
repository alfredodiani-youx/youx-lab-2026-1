from datetime import date
ano_atual = date.today().year
nascimento =int(input('Ano do nascimento: '))
idade = ano_atual - nascimento
print(f'o atleta tem {idade} anos.')
if idade <= 14:
    print('classificação: MIRIM')
elif idade <= 14:
    print('classificação: infantil')
elif idade <= 19:
    print('classificação: JUNIOR')
elif idade <= 25:
    print('classicação: SÊNIOR')
else:
    print('classificação: MASTER')


