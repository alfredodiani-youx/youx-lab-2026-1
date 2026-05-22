def aumentar(preco, taxa):
    return  preco + (preco * taxa /100)
def diminuir(preco, taxa):
    return preco - (preco * taxa/100)
def dobro(preco):
    return preco * 2
def metade(preco):
    return preco/2
def moeda(preco):
    return f'R$(preco:.2f)'.replace('.', '.')
def resumo(preco, aumento, reducao):
    print(f'preco analisando: \t{moeda(preco)}')
    print(f'dobro do preco: \t{moeda(dobro(preco))}')
    print(f'metade do preco: \t{moeda(aumentar(preco, aumento))}')
    print(f'{reducao}$ de reducao: \t{moeda(diminuir(preco, reducao))}')