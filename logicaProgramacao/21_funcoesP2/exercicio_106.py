comando = ' '
while comando != 'FIM':
    comando= input('funcao ou biblioteca >').upper()
    if comando != 'FIM':
        help(comando)
print('programa encerrado')