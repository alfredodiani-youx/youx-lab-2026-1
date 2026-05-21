from datetime import date
ano = int(input('insira o ano que desejas analisar coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('o ano {} E BISSEXTO'.format(ano))
else:
    print('o ano {} NÃO E BISSEXTO'.format(ano))