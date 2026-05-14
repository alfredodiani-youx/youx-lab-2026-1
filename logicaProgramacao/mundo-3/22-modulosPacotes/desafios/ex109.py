def aumentar(v, p, formato=False):
    preco = v + (v * p/100)
    if formato == True:
        preco = f'R${preco:.2f}'
    return preco

def reduzir(v, p, formato=False):
    preco = v - (v * p/100)
    if formato == True:
        preco = f'R${preco:.2f}'
    return preco

def dobro(v, formato=False):
    preco = v * 2
    if formato == True:
        preco = f'R${preco:.2f}'
    return preco

def metade(v,formato=False):
    preco = v / 2
    if formato == True:
        preco = f'R${preco:.2f}'
    return preco

def moeda(v):
    preco = f'R${v:.2f}'
    return preco