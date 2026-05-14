total= totmil= menor= cont= 0
barato= ' '
while True:
    prduto= str(input("nome do produto :"))
    preco= float(input("preço do produto :"))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = prduto
    resposta= ' '
    while resposta not in 'S/N':
        resposta= str(input('voce deseja continuar ? [S/N]')).strip().upper()
    if resposta == 'N':
        break
print(f'o total da compra é {total}')
print(f'no total {totmil} produtos custam mais de 1000 reais')
print(f'o produto mais barato é {menor}')