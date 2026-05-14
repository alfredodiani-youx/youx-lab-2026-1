preco=float(input('Qual o preço do produto? '))
print("""formas de pagamento: 
[1] DINHEIRO/ CHEQUE
[2] CARTÃO """)
pgt=int(input('Qual a forma de pagamento? '))
valor_final=None
if pgt == 1:
    valor_final= preco - (preco*10/100)
elif pgt ==2:
    print('Em quantas vezes você que pagar no cartão?\ndigite [1] para a vista, ou digite a quantidade de parcelas.')
    qtd_parcelas=int(input('R: '))
    if  qtd_parcelas==1:
        valor_final=preco-(preco*5/100)
    elif qtd_parcelas==2:
        valor_final=preco
    elif qtd_parcelas >2:
        valor_final=preco+(preco*20/100)
    else:
        print('Quantidade de parcelas invalida.')
else:
    print('Você digitou uma opção invalida.')

if valor_final:
    print(f'O valor final a ser pago é {valor_final}')
else:
    print('ocorreu um erro.')