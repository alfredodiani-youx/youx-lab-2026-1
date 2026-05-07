salario =float(input(' qual é o salario do funcionário? R$'))
novo = salario +(salario * 15/100)
print(' um funcionario que ganhava R${:.2f}, com 15% de aumento passa a receber R${:.2f}'.format(salario,novo))