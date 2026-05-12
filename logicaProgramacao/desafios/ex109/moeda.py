def aumentar(valor,num, sit=False):
    preco = valor + (num * (valor/100))
    if sit == True:
        preco = f'R${preco:.2f}'
    return preco

def diminuir(valor, num, sit=False):
    preco = valor - (num * (valor/100))
    if sit == True:
        preco = f'R${preco:.2f}'
    return preco

def dobro(valor, sit=False):
    preco = valor * 2
    if sit == True:
        preco = f'R${preco:.2f}'
    return preco

def metade(valor, sit=False):
    preco = valor / 2
    if sit == True:
        preco = f'R${preco:.2f}'
    return preco

def moeda(preco):
    preco = f'R${preco:.2f}'
    return preco