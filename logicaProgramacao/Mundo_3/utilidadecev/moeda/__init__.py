
def aumentar(preco=0, taxa=0, formato=False):
    res = preco + (preco * taxa / 100)
    return res if formato is False else moeda(res)

def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa / 100)
    return res if formato is False else moeda(res)

def dobro(preco=0, formato=False):
    res = preco * 2
    return res if not formato else moeda(res)

def metade(preco=0, formato=False):
    res = preco / 2
    return res if not formato else moeda(res)

def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.','.')

def resumo(v, a, r):
    print(f'{'Resumo do valor':^30}')
    print(f'Preço analizado: R${v:.2f}')
    print(f'Dobro do preço: R${v*2:.2f}')
    print(f'Metade do preço: R${v/2:.2f}')
    print(f'{a}% de aumento: R${v + (v*a/100):.2f}')
    print(f'{r}% de reduçao: R${v - (v*r/100):.2f}')