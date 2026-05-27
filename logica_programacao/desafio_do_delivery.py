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

print("Bem vindo!")

nome = str(input("Digite seu nome:"))
id_do_cardapio = "id"
soma_do_total = 0
opcao = 0

while opcao != 4:
    print("O que deseja?:")
    print("""
    [1] Ver Cardápio e Avaliações
    [2] Adicionar Item ao Pedido
    [3] Finalizar Pedido
    [4] Sair do Sistema
    """)
    opcao = int(input("Escolha: "))
    if opcao == 1:
        for inf in cardapio:
            print(inf)
    if opcao == 2:
        codigo_identificacao = int(input("Qual o ID do produto desejado?:"))
        carrinho = []
        while codigo_identificacao <= 0 or codigo_identificacao >=11:
            print("Esse produto não existe...Tente novamente!")
            codigo_identificacao = int(input("Qual o ID do produto desejado?:"))
            if codigo_identificacao >=1 or codigo_identificacao <=10:
                quantidade = int(input("Qual a quantidade desejada?:"))
                carrinho.append(codigo_identificacao * quantidade)
                print("Item adicionado ao carrinho de compras!")
                print(carrinho)
    #if opcao == 3:

    if opcao == 4:
        print("Encerrado!")
        print("Volte sempre!")

#nao fiz a 3 pois estava melhorando a 2 para encaixar na 3...


















