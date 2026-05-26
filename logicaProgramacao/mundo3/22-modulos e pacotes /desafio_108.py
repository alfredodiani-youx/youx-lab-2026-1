# --- FUNÇÕES ---
def aumentar(preco = 0, taxa = 0):
    res = preco + (preco * taxa / 100)
    return res

def diminuir(preco = 0, taxa = 0):
    res = preco - (preco * taxa / 100)
    return res

def dobro(preco = 0):
    res = preco * 2
    return res

def metade(preco = 0):
    res = preco / 2
    return res

def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')

# --- PROGRAMA PRINCIPAL ---
p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda(p)} é {moeda(metade(p))}')
print(f'O dobro de {moeda(p)} é {moeda(dobro(p))}')
print(f'Aumentando 10%, temos {moeda(aumentar(p, 10))}')