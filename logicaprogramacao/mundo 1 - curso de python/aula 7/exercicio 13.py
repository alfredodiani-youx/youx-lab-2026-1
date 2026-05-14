salário = float(input('Qual é o salário do funcionário? R$'))
novo = salário + (salário * 15 / 100)
print('Um funcionário que ganhava R${}, com 15% de aumento, passa a receber R${}'.format(salário, novo))
