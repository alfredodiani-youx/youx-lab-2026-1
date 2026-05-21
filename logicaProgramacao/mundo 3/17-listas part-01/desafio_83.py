lista = []
expressao = input('Digite sua expressao: ')
for e in expressao:
    if e == '(':
        lista.append(e)
    elif e == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Expressao valida! ')
else:
    print('Expressao incorreta! ')