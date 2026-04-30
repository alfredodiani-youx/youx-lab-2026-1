ano = int(input('Que ano quer analisar?'))
if ano % 4 == 0 and ano % 100 != 0 or ano %  400 == 0:
    print('O ano {} e bissexto!'.format(ano))
else:
    print('O ano {} nao e bissexto!'.format(ano))
