import calendar

ano = int(input('Digite um ano: '))
if calendar.isleap(ano):
    print('{} e bissexto' .format(ano))
else:
    print('{} não e bissexto' .format(ano))