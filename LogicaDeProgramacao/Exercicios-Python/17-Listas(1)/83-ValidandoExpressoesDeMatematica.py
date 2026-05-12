expr = str(input('Digite sua expressão: '))
e1 = expr.count('(')
e2 = expr.count(')')
if e1 == e2:
    print('Expressão valida')