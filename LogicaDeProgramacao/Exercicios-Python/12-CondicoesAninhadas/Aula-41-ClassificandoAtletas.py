from datetime import date
idade = int(input('Ano de nascimento: '))
anoAtual = date.today().year
totalIdade = anoAtual - idade
if totalIdade <= 9:
    print('MIRIM')
elif totalIdade <= 14:
    print('INFANTIL')
elif totalIdade <= 19:
    print('JÚNIOR')
elif totalIdade <= 25:
    print('SÊNIOR')
elif totalIdade > 25:
    print('MASTER')
else:
    print('ERRO')