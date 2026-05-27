cardapio = [
    {
        "id": 1,
        "nome": "Hambúrguer Clássico",
        "preco": 25.50,
        "avaliacoes": [5, 4, 5]
    },
    {
        "id": 2,
        "nome": "Pizza Margherita",
        "preco": 45.00,
        "avaliacoes": [5, 5, 4, 4, 5, 4]
    },
    {
        "id": 3,
        "nome": "Batata Frita",
        "preco": 15.00,
        "avaliacoes": [3, 4]
    },
    {
        "id": 4,
        "nome": "Refrigerante Lata",
        "preco": 8.00,
        "avaliacoes": [5, 5, 5, 4]
    },
    {
        "id": 5,
        "nome": "Cachorro Quente Prensado",
        "preco": 18.90,
        "avaliacoes": [4, 4, 5, 3]
    },
    {
        "id": 6,
        "nome": "Suco de Laranja Natural",
        "preco": 12.00,
        "avaliacoes": [5, 5, 5]
    },
    {
        "id": 7,
        "nome": "Sorvete de Baunilha",
        "preco": 14.50,
        "avaliacoes": [5, 4, 5, 5]
    },
    {
        "id": 8,
        "nome": "Porção de Onion Rings",
        "preco": 22.00,
        "avaliacoes": [4, 3, 4, 4, 5]
    },
    {
        "id": 9,
        "nome": "Salada Caesar",
        "preco": 28.00,
        "avaliacoes": [5, 5, 4]
    },
    {
        "id": 10,
        "nome": "Brownie de Chocolate",
        "preco": 16.00,
        "avaliacoes": [5, 5, 5, 5, 4]
    }
]


resp = None
soma_pedido = 0
soma_avali = 0
avali = []
id_pe = []
quant = []
escolha = 0
while escolha != 4:
    print('[1] Ver Cardápio e Avaliações\n[2] Adicionar Item ao Pedido\n[3] Finalizar Pedido\n[4] Sair do Sistema')
    escolha = int(input('R: '))
    for c in cardapio:
            if escolha == 1:
                #avali.append(c['avaliacoes'])
                avali += c['avaliacoes']
                soma_avali = sum(avali)/len(avali)
                print('-'*24)
                print(f"""id:[{c['id']}]\n{c['nome']}\npreço:{c['preco']}R$\navaliações : {soma_avali:.1f}""")
                print('-' * 24)
            if escolha == 2:
                while resp != 'N':
                    id_pe = int(input('Qual o id do pedido? '))
                    if id_pe == c['id']:

                        quant = int(input('Quantidade: '))

                        # while quant >= 0:
                            #if quant == 0
                          # if quant >= 1:
                              #soma_pedido = quant * c['preco']
                            # print('Adicionado ao carriho')
                            # resp = 'N'
                    #else:
                    #     print('ERRO! digite o id ')
                    #     quant = int(input('R:'))
                    #     if quant >= 1:
                    #         resp = 'N'

