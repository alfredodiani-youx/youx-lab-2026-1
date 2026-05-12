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

def resumo(valor, aumento, reducao):
    print(f'{'Resumo do valor':^30}')
    print(f'Preço analisado:            R${valor}')
    print(f'Dobro do preço:             R${moeda(dobro(valor))}')
    print(f'Metade do preço:            R${moeda(metade(valor))}')
    print(f'{aumento}% de aumento:             R${moeda(aumentar(valor, aumento))}')
    print(f'{reducao}% de redução:             R${moeda(diminuir(valor, reducao))}')