nome = str(input('qual seu nome?'))
if nome == 'Marjori':
    print('Que nome bonito!')
    print(f'tenha um bom dia, {nome}!')
elif nome == 'Pedro' or nome == 'Ana'or nome == 'Gabriel':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Claudia Ana Julia ':
    print('belo nome feminino!')
else:
    print('seu nome é bem normal.')
print(f'tenha um bom dia,{nome}! ')