#Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.
p1000 = 0
total = 0
barato = 0
cont = 0
print("LOja de produtos")
while True:
    nome_p = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: R$"))
    total += preco
    cont += 1
    if preco >= 1000:
        p1000 += 1
    if cont == 1:
        barato = preco
    else:
        if preco < barato:
         barato += preco
    r = input("Voce deseja continuar:[S/N] ").upper()
    if r == 'N':
        break


print(f"O preço total dos produtos R${total:.2f} \n O produto mais barato custou R${barato} \n E a quantidade de produtos que passam dos 1000 reais foi {p1000}")
