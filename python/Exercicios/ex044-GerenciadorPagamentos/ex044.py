preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual a opção da forma de pagamento? '))

if opcao == 1:
    desconto = (preco*10)/100
    print('Sua compra de R${} vai custar R${:.2f}'.format(preco , preco - desconto))
elif opcao == 2:
    desconto = (preco*5)/100
    print('Sua compra de R${} vai custar R${:.2f}'.format(preco , preco - desconto))
elif opcao == 3:
    parcela = (preco / 2)
    print('Sua compra será dividida em duas parcelas de R${:.2f}'.format(parcela))
    print('Sua compra de R${} vai custar R${:.2f}'.format(preco , preco))
elif opcao == 4:
    precototal = preco + ((preco*20)/100)
    numparcelas = int(input('Quantas parcelas? '))
    parcela = precototal / numparcelas
    print('Sua compra será dividida em {} parcelas de R${:.2f}'.format(numparcelas , parcela))
    print('Sua compra de R${:.2f} vai custar R${:.2f}'.format(preco , precototal))
else:
    print('Escolha umas das opções entre 1 e 4')
