expressao =str(input('digite uma expressao: '))
cont = 0
for c in expressao:
    if c == "(":
        cont += 1
    elif c == ")":
        cont -= 1
        if cont < 0:
            break
if cont == 0:
    print('espressao valida')
else:
    print('espressao invalids')