def leiaInt(a: str):
    while True:
        valor = input(a)
        if valor.isnumeric():
            return int(valor)
        else:
            print('eRRO! Digite um número válido')
n = leiaInt('Digite um valor: ')
print(f'Você acabou de digitar o número {n}')