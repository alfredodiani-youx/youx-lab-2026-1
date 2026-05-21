produtos = ('lapis', 1.75,
            'borracha',1.50,
            'cardeno',20.00,
            'estojo',25.00,
            'transfiridor',5.20,
            'compasso', 9.50,
             'mochila', 150.00,
             'livros', 300.00 )
for i in range(0,len(produtos)):
    if i % 2 == 0 :
        print(f'{produtos[i]:.<30} = ', end= '')
    else:
        print(f'R${produtos[i]}')