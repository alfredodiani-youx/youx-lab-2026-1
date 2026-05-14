def leiaDinheriro(valor):
    valido = False
    while not valido:
        valor = input(valor)
        if valor.isalpha() or valor.strip() == '':
            print(f'ERRO! {valor} é um preço inválido.')
        else:
            valido = True
            return float(valor)