preco = float(input('Qual é o preço das compras? R$'))
print(''''Escolha uma forma de pagamento?:
[1] á vista dinheiro/cheque
[2] á vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção?'''))
if opcao == 1:
    total = preco - ( preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
elif opcao == 4:
    total = (preco * 0.20)
print(f"Sua compra de {(preco):.2f} no final vai custar {(total):.2f}")