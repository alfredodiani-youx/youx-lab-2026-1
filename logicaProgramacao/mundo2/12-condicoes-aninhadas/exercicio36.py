casa= float(input(' valor da casa: R$'))
salario =float(input('qual é o seu salario? R$'))
anos =int(input(' em quantos anos vocẽ vai pagar?'))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print('para pagar uma casa de R${:.2f} em {} anos '.format(casa, anos), end='' )
print('a prestação sera de R${:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('EMPRETISMO PODE SER  CONCEDIDO!')
else:
    print('EMPRETISMO NEGADO!')





