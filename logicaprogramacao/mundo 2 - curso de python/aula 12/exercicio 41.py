import datetime

ano_de_nascimento = int(input('Ano de nascimento: '))
ano_atual = datetime.date.today().year
idade = ano_atual - ano_de_nascimento
if idade <= 9:
    print('A categoria é MIRIM.')
elif idade <= 14:
    print('A categoria é INFANTIL.')
elif idade <= 19:
 print('A categoria é JUNIOR.')
elif idade <= 25:
 print('A categoria é SÊNIOR')
elif idade > 25:
 print('A categoria é MASTER.')