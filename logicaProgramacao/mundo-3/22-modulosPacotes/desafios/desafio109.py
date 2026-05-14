import ex109

preco = int(input('Digite um preço: R$'))
print(f'Aumentando 10%, temos {ex109.aumentar(preco, 10, True)}')
print(f'Reduzindo 10%, temos {ex109.reduzir(preco, 10, True)}')
print(f'O dobro de {ex109.moeda(preco)} é {ex109.dobro(preco, True)}')
print(f'A metade de {ex109.moeda(preco)} é {ex109.metade(preco, True)}')