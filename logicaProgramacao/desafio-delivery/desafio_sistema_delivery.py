from time import sleep
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
pedido_final = {}
itens = []
total = 0
desconto = 0
valor_entrega = 6

print('Boas vindas')
nome = str(input('Qual é seu nome? '))
pedido_final['Nome_cliente'] = nome

while opcao != 4:
    if len(pedido_final) == 0:
        nome = str(input('Qual é seu nome? '))
        pedido_final['Nome_cliente'] = nome

    print('''
    [1] Ver Cardápio e Avaliações.
    [2] Adicionar item ao pedido.
    [3] Finalizar pedido.
    [4] Sair do Sistema.''')
    opcao = int(input('O que deseja fazer? '))
    if opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4:
        print('Comando inválido. Tente novamente.')
        opcao = int(input('O que deseja fazer? '))

    if opcao == 1:
        for itens in cardapio:
            soma = 0
            contador = 0
            for av in itens['avaliacoes']:
                soma += av
                contador += 1
            print(f'Id: {itens['id']}. {itens['nome']}. Preço: {itens['preco']} Avaliação: {soma / contador:.1f}')

    elif opcao == 2:
        id = int(input('Id do pedido: '))
        quantidade = int(input('Quantidade: '))
        for item in cardapio:
            carrinho = {}
            if item['id'] == id:
                carrinho['nome'] = item['nome']
                carrinho['quantidade'] = quantidade
                carrinho['preco'] = item['preco']
                preco = item['preco'] * quantidade
                total += preco
                itens.append(carrinho)
                pedido_final['itens'] = itens

    elif opcao == 3:
        if total > 75:
            pedido_final['subtotal'] = f'R${total - (total * 15/100):.2f}'
            desconto = total - (total * 15/100)
        elif total > 50 and total < 75:
            pedido_final['subtotal'] = f'R${total - (total * 10/100):.2f}'
            desconto = total - (total * 10 / 100)
        pedido_final['valor_entrega'] = f'R${valor_entrega:.2f}'
        pedido_final['valor_total'] = f'R${desconto + valor_entrega:.2f}'
        print('Gerando pedido e enciando para cozinha... ')
        sleep(0.5)
        print(pedido_final)
        pedido_final.clear()
        itens.clear()
        total = 0
        desconto = 0
        sleep(0.5)
print('Obrigado pelo pedido. Volte sempre')