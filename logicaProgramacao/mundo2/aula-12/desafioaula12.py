nome = str(input('Qual e o seu nome? '))
if nome == 'maria':
    print('Que nome lindo!')
elif nome == 'Julia' or nome =='Eduarda' or nome == 'Jessica':
    print('Seu nome e bem comum no Brasil!')
elif nome in 'Olivia Mayara juliana':
    print('belo nome!')
else:
    print('Seu nome nao e tao bonito assim!')
print(f'Tenha um bom dia {nome}!')