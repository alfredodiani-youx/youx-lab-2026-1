
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



pedido_final= {}
dicionario ={}
carrinho = []
opcao = ''
print("Bem vindo ao restaurante")
nome = input("Por favor, digite o seu nome: ").capitalize()
while opcao != '4':
    print("[1] VER CARDAPIO E AVALIAÇOES \n [2] ADICIONAR ITEM AO PEDIDO \n [3] FINALIZAR PEDIDO \n [4] Sair do programa")
    opcao = input("")
    if opcao == '1':
        for alimento in range (0, len(cardapio)):
            print(f'id: {cardapio[alimento]['id']} | {cardapio[alimento]['nome']} | preço: R${cardapio[alimento]['preco']:.2f}')

    elif opcao =='2':

        requisicaoID = int(input("Digite o id do alimento: "))
        for id in range(0, len(cardapio)):
            cont = 0
            if requisicaoID == cardapio[id + cont]['id']:
                print(cardapio[id]['nome'])
                quantidade = int(input("Digite a quantidade de produtos: "))
                dicionario['quantidade'] = quantidade
                dicionario['nome'] = cardapio[id]['nome'],
                dicionario['preco'] = cardapio[id]['preco']
                carrinho.append(dicionario.copy())
                dicionario.clear()
        print(carrinho)

    elif opcao =='3':
        total = 0
        soma = 0
        for p in range(len(carrinho)):
            preco_quantidade = carrinho[p]['preco'] * carrinho[p]['quantidade']
            total += preco_quantidade
            p+=1
            pedido_final['subtotal'] = total
            pedido_final['valor_entrega'] = 6.00

            if total > 75.00:
                total = total -( total *15/100) +6
                pedido_final['valor_total'] = total

            elif total > 50.00:
                total = total - (total*10/100) +6
                pedido_final['valor_total'] = total
        pedido_final['nome_cliente'] = nome
        pedido_final['itens'] = carrinho
        print("Gerando o pedido e enviando para a cozinha")
    elif opcao ==4:
        print(f"Volte sempre{nome}")

    else:
        pass

print(pedido_final)

