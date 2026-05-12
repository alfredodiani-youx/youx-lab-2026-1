def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg).strip().replace(',','.'))
        if entrada.isalpha() or entrada == '':
            print(f'\033[91m"{entrada}" não é um valor monetário.\033[m')
        else:
            valido = True
            return float(entrada)