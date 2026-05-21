salario = float(input('Qual é o salario do Funcionario? ' ))
novo = salario + (salario * 10 / 100)
print('quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(salario, novo))