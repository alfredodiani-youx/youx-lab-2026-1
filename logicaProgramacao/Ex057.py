G = str(input('Informe o seu genero [M/F]: ')).strip().upper()
while G not in ('M' or 'F'):
    G = str(input('Esta incorreto,por favor digite novamente: ')).strip().upper()
print(f'Opcao {G} confirmada')