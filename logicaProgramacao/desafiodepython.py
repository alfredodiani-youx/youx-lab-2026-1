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

print('=-' * 30)
print('HANBURQUEIRA DA ANA ')
print('-='* 30)
nome =str(input('seja bem vindo! pode digitar seu nome por favor:'))
opcao = 0
carrinho = []

while opcao != 4:
    print('-='* 30)
    print('[1] ver cardárpio e avaliações')
    print('[2] adicionar item ao pedido')
    print('[3] finalizar pedido')
    print('[4] sair do sistema  ')
    opcao =int(input('qual é sua opção? '))
    print('-='* 30)
    if opcao == 1:
        for i in cardapio:
            soma = 0
            print(f"Id: {i['id']}")
            print(f"Nome: {i['nome']}")
            print(f"Preço: {i['preco']}")
            for valores in i['avaliacoes']:
                soma += valores
            media = soma / len(i['avaliacoes'])
            print(f"Media de avaliações: {media:.2f}")
            print('-='*30)

     elif opcao == 2:
          qual_id = int(input('qual o id do item desajado?'))
            quantidade = int(input('quantidade: '))
    #     for i in cardapio:





    # elif opcao == 3:
    #     print()
    #





    elif opcao == 4:
        print('finalizado')
    else:
        print('opção invalida ,digite novamente')
print('saindo do siatema')
