#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

#  à vista dinheiro/cheque: 10% de desconto
#  à vista no cartão: 5% de desconto
#  em até 2x no cartão: preço formal
#  3x ou mais no cartão: 20% de juros
preco = float(input("Qual o valor da compra: R$ "))
print("Escolha a forma de pagamento \n [1] À vista dinheiro/cheque \n [2] À vista cartao \n [3] 2x no cartao \n [4] 3x ou mais no cartao ")
opcao = int(input(""))
if opcao == 1:
    desconto = preco - ( preco * 10 / 100 )
    print(f"Sua compra de R${preco:.2f} sairá a R${desconto:.2f}")
elif opcao == 2:
    desconto = preco - ( preco * 5 / 100 )
    print(f"Sua compra de R${preco:.2f} sairá a R${desconto:.2f}")
elif opcao == 3:
    print(f"Sua compra sairá R${preco:.2f}")
elif opcao == 4:
    juros = preco + (preco * 20 / 100 )
    print(f"Sua compra de R${preco:.2f} com juros de 20% sairá a R${juros:.2f}")

else:
    print("Opçao invalida")