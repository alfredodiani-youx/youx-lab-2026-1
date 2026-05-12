def aumentar(preco,num):
    preco += (num * (preco/100))
    return preco

def diminuir(preco, num):
    preco -= (num * (preco/100))
    return preco

def dobro(preco):
    igual = preco * 2
    return igual

def metade(preco):
    igual = preco / 2
    return igual

def moeda(preco):
    preco = f'R${preco:.2f}'
    return preco