#Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:

    #à vista dinheiro/cheque: 10% de desconto
    #à vista no cartão: 5% de desconto
    #em até 2x no cartão: preço formal
    #3x ou mais no cartão: 20% de juros


valor = float(input("Qual o valor do produto? "))

print('''
    [1] à vista dinheiro/cheque: 10% de desconto
    [2] à vista no cartão: 5% de desconto
    [3] em até 2x no cartão: preço formal
    [4] 3x ou mais no cartão: 20% de juros
    ''')
opcao = int(input("Qual a opção de pagamento? "))
if opcao == 1:
    print(f"O valor a ser pago antes era de R${valor:.2f} e agora sera de R${valor * 0.9}")
elif opcao == 2:
    print(f"O valor a ser pago antes era de R${valor:.2f} e agora sera de R${valor * 0.95}")
elif opcao == 3:
    print(f"O valor de cada parcela vai ser de R${valor / 2}")
elif opcao == 4:
    print(f"O valor a ser pago agora é de R${valor * 1.2}")
