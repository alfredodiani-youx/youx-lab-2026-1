nome = str(input('Como você chama? ')).lower().strip()

if nome == 'beatriz':
    print('é um nome muito bonito!')
elif nome == 'pedro' or nome == 'lara' or nome == 'bia':
    print('seu nome é bem popular entre os brasileiros')
else:
    print('seu nome é bem comum.')

print('tenha uma boa tarde {}'.format(nome))
