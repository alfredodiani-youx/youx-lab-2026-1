preco = float(input('qual o preço das compras:'))
print('''formas de pagamento
[1] a vista dinheiro/cheque
[2] a vista no cartao
[3] ate 2x no cartao 
[4] 3x ou mais no cartao ''')
opcao = int(input('qual opçao voce prefere?  '))
if opcao == 1:
    total = preco * 0.90
elif opcao == 2:
    total = preco * 0.95
elif opcao == 3:
    total = preco
elif opcao == 4:
    total = preco * 0.80
print(total)
