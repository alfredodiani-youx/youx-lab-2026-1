nome = str(input('Digite seu nome: ')).strip().upper()
if nome == 'ARTUR':
    print('Eita, nome mais lindo q ja vi em toda minha vida')
elif nome == 'LUIZ' or nome == 'MARIA':
    print('Eh, nome bem comum...')
elif nome in 'ANA JOAO GABRIEL':
    print('Éh, nome legalzinho...')
else:
    print('ah, nome meio sem graça, mas...')
print('Bom dia, {}!'.format(nome))
