import colorsys
# ---------------------------------- <> ---------------------------------- #

def valor(valor1 = 0, reais = 'R$'):
    return (f'{reais}{valor1}')


def metade(valor1 = 0, format = False):
    res = valor1 / 2
    return res if format is False else valor(res)


def dobro(valor1 = 0, format = False):
    res = valor1 * 2
    return res if format is False else valor(res)


def aumento(valor1 = 0,valor2 = 0, format = False):
    res = valor1 + (valor1 * valor2 / 100)
    return res if format is False else valor(res)

def leia(valor1):
    if valor1
def resumo(valor1='',valor2=0,valor3=0):
    print('-'*30)
    print('        Resumo Do Valor')
    print('-'*30)
    print(f'Preço analisado:  R${valor1}')
    dobro = valor1 * 2
    print(f'Dobro preço:      R${dobro}')
    metade = valor1 / 2
    print(f'Metade preço:     R${metade}')
    aum = valor1 + (valor1 * valor2 / 100)
    print(f'{valor2}% de aumento:   R${aum}')
    red = valor1 - (valor1 * valor2 / 100)
    print(f'{valor3}% de redução:   R${red}')
    print('-'*30)

# ---------------------------------- <> ---------------------------------- #