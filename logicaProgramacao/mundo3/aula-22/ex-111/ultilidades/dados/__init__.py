def leiaDinheiro(mensagem):
    válido = False
    while not válido:
        entrada = str(input('mensagem'))
        if entrada.isalpha():
            print('PREÇO INVALIDO! ')
        else:
            válido = True
            return  float(entrada)