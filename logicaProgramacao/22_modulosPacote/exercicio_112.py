def leiadinheiro(txt):
    while True:
        n = input(txt)
        n = n.replace(',', '.')
        if n.replace('.', '').isnumeric() and n.count('.') <= 1:
            return float(n)
        print(f'\033[31mO valor "{n}" é inválido.\033[m')
preco = leiadinheiro('digite o preço R$')
print(f'o preço digitado foi R${preco}')