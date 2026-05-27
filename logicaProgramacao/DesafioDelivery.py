from statistics import mean
carrinho = list()
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

print('-='*18)
print('Boas Vindas,Aproveite nossa Loja!')
print('-='*18)
sair = ''
nome = str(input('Digite seu nome: '))
print('-='*18)
while sair != '4':
    print('-=' * 18)
    print('[1] Ver cardapios e avaliacoes')
    print('[2] Adicionar item ao pedido')
    print('[3] Finalizar Pedido')
    print('[4] Sair do Sistema')
    print('-=' * 18)
    sair = int(input('Digite qual a opcao voce deseja: '))
    print('-=' * 18)

    if sair == 1:
        for item in cardapio:
            print(f'ID: {item["id"]} |',end=' ')
            print(f'NOME: {item["nome"]} |',end= ' ')
            print(f'PRECO: {item["preco"]} |',end=' ')
            media = mean(item["avaliacoes"])
            print(f'MEDIA_AVALIACOES: {media:.2f}')








