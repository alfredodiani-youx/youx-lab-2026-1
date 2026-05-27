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

opcao = 0
total = 0
nome = 'nome_usuario'
print('seja bem vindo!')
nome_usoario = str(input('qual é o seu nome ?'))
while opcao != 4:
    print('''
    [1] Ver Cardápio e Avaliações
    [2] Adicionar Item ao Pedido
    [3] Finalizar Pedido
    [4] Sair do Sistema''')
    opcao = int(input('qual sua escolha?'))
    if opcao  == 1:
        for item in cardapio:
            print(f'{item['id']} {item['nome']} {item['preco']} {item['avaliacoes']} ')
    elif opcao == 2:
        id = int(input('qual e o id ?'))
        quantidade = int(input('qual e a quantidade?'))
#nao consigui terminar 17:56

    elif opcao == 3:
        print(item)
    elif opcao == 4:
        print(item)
    else:
        print("errado")





