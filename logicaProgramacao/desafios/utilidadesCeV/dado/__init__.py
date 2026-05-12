def leiaDinheiro(preco):
    valido = False
    while not valido:
        valor = str(input(preco))
        if valor.isalpha() or valor.strip() == '':
            print('ERRO! Preço inválido!')
        else:
            valido = True
            return float(valor)