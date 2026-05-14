import ex107
preco = int(input('Digite o preço: R$'))
print(f'Aumentando em 10%, temos {ex107.aumentar(preco, 10)}')
print(f'Reduzindo em 10%, temos {ex107.reduzir(preco, 10)}')
print(f'O dobro de {preco} é {ex107.dobro(preco)}')
print(f'A metade de {preco} é {ex107.metade(preco)}')