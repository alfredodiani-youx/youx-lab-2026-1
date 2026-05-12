itens = ('Lapis', 1 ,
      'Caneta', 2 ,
      'Borracha',3 ,
      'Caderno', 4 ,
      'Livro', 5 ,)
print('-'*45)
for c in range(0, len(itens), 2):
    print(f'{itens[c]:.<34} ', end='')
    print(f'R$ {itens[c+1]:>7.2f}')
print('-'*45)







